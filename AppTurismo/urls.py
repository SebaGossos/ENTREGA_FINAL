from django.urls import path
from AppTurismo.views import *
urlpatterns = [
    path('', inicio, name='AppInicio'),
    
]
