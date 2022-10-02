from random import choices
from django.db import models
from django.contrib.auth.models import User
from AppTurismo.choices import lugares_para_viajar
from django.contrib.admin.widgets import  AdminDateWidget


class PaqueteTuristico(models.Model):    
    lugares = models.IntegerField(null=False,blank=False, choices=lugares_para_viajar, default=1)
    fecha_de_entrada = models.DateField()
    fecha_de_salida = models.DateField()
    empleado_asignado = models.CharField (max_length=33, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='paquetes')
    created_at = models.DateTimeField(auto_now_add=True)
   


    def __str__(self,):

        return f'Paquete: {self.lugares} Fexha de entrada: {self.fecha_de_entrada} Fecha de salida: {self.fecha_de_salida}'

class Cliente (models.Model):
    nombre = models.CharField(max_length=33)
    apellido = models.CharField(max_length=33)
    email = models.EmailField(unique=True)
    celular = models.PositiveIntegerField()
    dni = models.IntegerField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self, ):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Dni: {self.dni}'

class PaqueteAcompanante(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)    
    paquete_turistico = models.ForeignKey(PaqueteTuristico, on_delete= models.CASCADE, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
   
    
