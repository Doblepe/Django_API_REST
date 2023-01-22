from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, redirect
from django.conf import settings
import pandas as pd
import csv
import json
from myApp.serializer import irisSerializer
from rest_framework.response import Response

# TODO: importar Response


@api_view(['GET'])
def irisData(request):
    if request.method == 'GET':
        csv = settings.MEDIA_ROOT + '/iris.csv'
        csv = "/home/victorperez/Escritorio/Aplicaciones/Django_API_REST/my_projectWeb/media/iris.csv"
        df = pd.read_csv(csv)
        data = df.to_json(orient="index")
        data = json.loads(data)
        describe = df.describe().to_json(orient="index")
        describe = json.loads(describe)
        return render(request, "iris/main.html",
        context= {"data" : data, "describe":describe
        }, status= status.HTTP_200_OK)



@api_view(['GET', 'POST'])
def insertData(request):
    result = ''
    if request.method == 'GET':
        return render(request, "iris/insert.html")
    elif request.method == 'POST':
       data = request.data
       print(data)
       serializer = irisSerializer(data=data)
       
    if serializer.is_valid():
 # Guardamos los datos:
        serializer.save()
 # insertar dato en csv:
        X = settings.MEDIA_ROOT + '/iris.csv'
        with open(X, 'a', newline='') as csvfile:
            fieldnames = ['sepal_length', 'sepal_width',
            'petal_length', 'petal_width', 'species']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'sepal_length': data['sepal_length'],
                'sepal_width': data['sepal_width'],
                'petal_length': data['petal_length'],
                    'petal_width': data['petal_width'],
                 'species': data['species']})
            print("writing complete")
 # resultado que nos muestre si se ha insertado:
            result = 'Insertado correctamente'
        return render(request, 'iris/insert.html',
                context={'result': result}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
        
## 57,40


@api_view(['GET', 'PUT', 'POST'])
def updateData(request):
    if request.method == 'GET':
        csv = settings.MEDIA_ROOT +"/iris.csv"
        df = pd.read_csv(csv)
        last_data = df.iloc[-1]
        sepal_length = str(last_data["sepal_length"])
        sepal_width = str(last_data["sepal_width"])
        petal_length = str(last_data["petal_length"])
        petal_width = str(last_data["petal_width"])
        species = str(last_data["species"])
        return render(request, "iris/update.html", context={"sepal_length": sepal_length, 
        "sepal_width": sepal_width, "petal_length": petal_length, "petal_width": petal_width, 
        "species": species})
    # Lo probamos usando POSTMAN:
    elif request.method == 'PUT':
        data = request.data
        csv = settings.MEDIA_ROOT +"/iris.csv"
        df = pd.read_csv(csv)
        serializer = irisSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            df.loc[df.index[-1], "sepal_length"] =serializer.data["sepal_length"]
            df.loc[df.index[-1], "sepal_width"] = serializer.data["sepal_width"]
            df.loc[df.index[-1], "petal_length"] = serializer.data["petal_length"]
            df.loc[df.index[-1], "petal_width"] = serializer.data["petal_width"]
            df.loc[df.index[-1], "species"] = serializer.data["species"]
            df.to_csv(csv, index=False)
            return Response(df.loc[-1], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)        


    # Lo mismo que el método PUT pero a través del front-end:
    elif request.method == 'POST':
        data = request.data
        csv = settings.MEDIA_ROOT +"/iris.csv"
        df = pd.read_csv(csv)
        serializer = irisSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            df.loc[df.index[-1], "sepal_length"] = serializer.data["sepal_length"]
            df.loc[df.index[-1], "sepal_width"] = serializer.data["sepal_width"]
            df.loc[df.index[-1], "petal_length"] = serializer.data["petal_length"]
            df.loc[df.index[-1], "petal_width"] = serializer.data["petal_width"]
            df.loc[df.index[-1], "species"] = serializer.data["species"]
            df.to_csv(csv, index=False)
            return redirect('/iris/')
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)   


@api_view(['GET', 'DELETE', 'POST'])
def deleteData(request):
    if request.method == 'GET':
 # Ruta donde se encuentra nuestro archivo:
 # /home/<username>/atom/my_django_web/my_projectWeb/media/iris.csv
        X = settings.MEDIA_ROOT + '/iris.csv'
 # Cargamos el dataset con ayuda de pandas:
        X_df = pd.read_csv(X)
        lastDate = X_df.iloc[-1]
        sepal_length = str(lastDate['sepal_length'])
        sepal_width = str(lastDate['sepal_width'])
        petal_length = str(lastDate['sepal_width'])
        petal_width = str(lastDate['petal_width'])
        return render(request, 'iris/delete.html', context={
            'lastDate': lastDate, 'sepal_length': sepal_length,
            'sepal_width': sepal_width, 'petal_length': petal_length,
            'petal_width': petal_width})
 
    elif request.method == 'DELETE':
        X = settings.MEDIA_ROOT + '/iris.csv'
        df = pd.read_csv(X)
        df.drop(df.index[-1], inplace=True)
        df.to_csv(X, index=False)
        return Response(df.iloc[-1], status=status.HTTP_204_NO_CONTENT)
 # Lo mismo que el método DELETE pero a través del front-end:
    elif request.method == 'POST':
 # Ruta donde se encuentra nuestro archivo:
 # /home/<username>/atom/my_django_web/my_projectWeb/media/iris.csv
        X = settings.MEDIA_ROOT + '/iris.csv'
        df = pd.read_csv(X)
 # Eliminar la última fila
        df.drop(df.index[-1], inplace=True)
 # convertir a csv
        df.to_csv(X, index=False)
 # Redireccionamos a la página principal para comprobar el dataset:
    return redirect('/iris/')