from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from AppUser.forms import *



def login_request (request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            usuario = data.get('username')
            contrasena = data.get('password')
            
            user = authenticate(username=usuario, password=contrasena)
              
            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion Satisfactorio')
                return redirect('AppInicio')
            else:
                messages.info(request, 'Inicio de sesion Fallido. Verificar usuario o Contraseña')
                
                
        else:
            messages.info(request, 'Formulario incorrecto') 
    
    context = {
        'form': AuthenticationForm(),
        'Button_value': 'Login',
        'method': 'POST',
        'title': 'LOGIN',
        'info': 'Inicio de Sesion',
    }    
    
    return render(request, 'AppUser/formulario_universal.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.info(request, 'El Usuario ha sido registrado satisfactoriamente :)')
            return redirect('AppUserLogin')
        else:
            messages.info(request, 'Tu usuario fallo y  no pudo ser registrado :(')
            return redirect('AppUserRegister')
            
    context = {
        'form': UserRegisterForm(),
        'Button_value': 'Register',
        'method': 'POST',
        'title': 'REGISTER',
        'info': 'Registro de usuario',
    }
    return render(request, 'AppUser/formulario_universal.html', context)


@login_required
def edit_user(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            usuario.username = data.get('username')
            usuario.first_name = data.get('first_name')
            usuario.last_name = data.get('last_name')
            usuario.email = data.get('email')
            usuario.save()
            
    context = {
        'form': UserRegisterForm(
            initial={
                'username':usuario.username,
                'first_name': usuario.first_name,
                'last_name': usuario.last_name,
                'email': usuario.email
            }
        ),
        'Button_value': 'Edit',
        'method': 'POST',
        'title': 'EDITAR',
        'info': 'Edición de usuario',
    }
    return render(request, 'AppUser/formulario_universal.html', context)
    