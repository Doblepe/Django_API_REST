from django.urls import path, include
from myApp import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path("accounts/", include("django.contrib.auth.urls")),
    # TODO: Añadir las urls para accounts
    # TODO: Añadir las urls para register
    # TODO: Añadir las urls para iris
    # TODO: Añadir las urls para insertData
    # TODO: Añadir las urls para updateData
    # TODO: Añadir las urls para deleteData
]
