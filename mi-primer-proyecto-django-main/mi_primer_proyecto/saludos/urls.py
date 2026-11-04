from django.urls import path
from . import views

urlpatterns = [
    path('', views.saludo, name='saludo'),           # /saludos/
    path('adios/', views.adios, name='adios'),       # /saludos/adios/  (reto adicional)
]
