from django.db import models




class PaqueteTuristico (models.Model):    
    lugares = models.CharField(max_length= 33)
    fecha_de_entrada = models.DateField()
    fecha_de_salida = models.DateField()


class Cliente (models.Model):
    nombre = models.CharField(max_length=33)
    apellido = models.CharField(max_length=33)
    email = models.EmailField(unique=True)
    celular = models.PositiveIntegerField()
    dni = models.IntegerField(unique=True)
    empleado_asignado = models.CharField (max_length=33)
    

    
    
    
