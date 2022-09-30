from django.db import models
from django.contrib.auth.models import User


class PaqueteTuristico(models.Model):    
    lugares = models.CharField(max_length= 33)
    fecha_de_entrada = models.DateField()
    fecha_de_salida = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Cliente (models.Model):
    nombre = models.CharField(max_length=33)
    apellido = models.CharField(max_length=33)
    email = models.EmailField(unique=True)
    celular = models.PositiveIntegerField()
    dni = models.IntegerField(unique=True)
    empleado_asignado = models.CharField (max_length=33)
    

    def __str__(self, ):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Dni: {self.dni}'


    
    
    
