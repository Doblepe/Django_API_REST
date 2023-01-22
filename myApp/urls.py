from django.urls import path, include
from myApp import views
from myApp.iris.views import irisData, insertData, updateData, deleteData


urlpatterns = [
    #He añadido una ruta por defecto para que redirija a home nada más cargar la aplicación
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name= 'register'),
    path("iris/", irisData, name= "iris"),
    path("insertData/", insertData, name= "insertData"),
    path("updateData/", updateData, name= "updateData"),
    path("deleteData/", deleteData, name="deleteData")

    # TODO: Añadir las urls para register
    # TODO: Añadir las urls para iris
    # TODO: Añadir las urls para insertData
    # TODO: Añadir las urls para updateData
    # TODO: Añadir las urls para deleteData
]
