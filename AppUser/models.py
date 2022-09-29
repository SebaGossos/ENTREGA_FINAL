
from django.db import models
from django.contrib.auth.models import User
from AppTurismo.models import *


class Comentario(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    paquete_truistico = models.OneToOneField(PaqueteTuristico, null=True, blank=True, on_delete=models.CASCADE)
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

 