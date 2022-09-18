from django.urls import path
from AppTurismo.views import *
urlpatterns = [
    path('', inicio, name='AppInicio'),
    path('paquete/', paquete_turistico, name='AppTurismoPaquete'),
    path('cliente/', cliente, name= 'AppCliente')  
]
