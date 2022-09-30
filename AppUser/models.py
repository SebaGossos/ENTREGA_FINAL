
from django.db import models
from django.contrib.auth.models import User
from AppTurismo.models import PaqueteTuristico



class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.CharField(max_length= 150)
    paquete_turistico = models.OneToOneField(PaqueteTuristico, on_delete=models.CASCADE, null=True, blank=True)
    

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

 