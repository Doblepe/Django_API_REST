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
        # TODO: mostrar el último dato del dataset update.html
        pass
    # Lo probamos usando POSTMAN:
    elif request.method == 'PUT':
        # TODO: actualizar el último dato del csv
        pass
    # Lo mismo que el método PUT pero a través del front-end:
    elif request.method == 'POST':
        # TODO: actualizar el último dato del csv
        pass


@api_view(['GET', 'DELETE', 'POST'])
def deleteData(request):
    if request.method == 'GET':
        # TODO: mostrar el último dato del dataset en la plantilla delete.html
        pass
    # Lo probamos usando POSTMAN:
    elif request.method == 'DELETE':
        # TODO: eliminar el último dato del csv
        pass
    # Lo mismo que el método DELETE pero a través del front-end:
    elif request.method == 'POST':
        # TODO: eliminar el último dato del csv
        pass
