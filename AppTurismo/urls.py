from django.urls import path
from AppTurismo.views import *
urlpatterns = [
    path('', inicio, name='AppInicio'),
    path('paquete/', paquete_turistico, name='AppTurismoPaquete'),
    path('cliente/', cliente, name= 'AppCliente'),
    path('busqueda_peticion', busqueda_de_peticion, name='AppBusquedaPeticion'),
    path('busqueda_peticion_post/', busqueda_peticion_post, name='AppBusquedaPeticionPost'),
    path('eliminar_peticion/<int:dni>', elminar_peticion, name='AppEliminarPeticion'),
]
