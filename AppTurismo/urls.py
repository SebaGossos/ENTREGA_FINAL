from django.urls import path
from AppTurismo.views import *
urlpatterns = [
    path('', inicio, name='AppInicio'),
    path('paquete/', paquete_turistico, name='AppTurismoPaquete'),
    path('cliente/', cliente, name= 'AppCliente'),
    path('eliminar_peticion/<int:dni>', elminar_peticion, name='AppEliminarPeticion'),
    path('editar_cliente/<int:dni>', editar_cliente, name= 'AppEditarAcompanante'),
    path('agregar_acompñante/',agregar_acompañantes, name='AppAgregarAcompañantes'),
    path('paquetes_contratados/', paquete_contratado, name='AppPaqueteContratado'),
    path('eliminar_paquete/<int:id> <int:dni>', eliminar_paquete, name='AppEliminarPaquete'),
    path('politica_de_privacidad/', politica_de_privacidad, name='AppPoliticaDePrivacidad'),
    path('acerca_de_mi/', acerca_de_mi, name='AppAcercaDeMi'),
    
    
] 
