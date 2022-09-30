from enum import unique
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from AppUser.models import *



class AvatarForm(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ('imagen',)

class UserRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(label='Nombres')
    last_name = forms.CharField(label='Apellidos')
    email = forms.EmailField(label='Email')
    celular = forms.IntegerField(label='Celular')
    dni = forms.IntegerField( label='Dni')
    username = forms.CharField(label='Usuario')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repetir la Contraseña', widget=forms.PasswordInput, required=False)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'celular', 'dni', 'password1', 'password2')