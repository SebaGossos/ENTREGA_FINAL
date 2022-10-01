import re
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from AppUser.models import Comentario
from AppTurismo.forms import *
from AppTurismo.models import *
import random
from datetime import date, datetime



@login_required
def inicio(request):
    return render(request, 'index.html')

@login_required
def paquete_turistico (request):
    
    if request.method == 'POST':
        
        mi_formulario = PaqueteTuristicoFormulario(request.POST)
        mi_formulario1 = ComentarioFormulario(request.POST)

        if mi_formulario.is_valid() and mi_formulario1.is_valid():
            
            data = mi_formulario.cleaned_data
            data1 =  mi_formulario1.cleaned_data
            


            paquete1 = PaqueteTuristico(lugares=data.get('lugares'), fecha_de_entrada=data.get('fecha_de_entrada'),
                                        fecha_de_salida=data.get('fecha_de_salida'), user=request.user)
            paquete1.save()
            
            comentario1 = Comentario(user=request.user, comentario= data1.get('comentario'),paquete_turistico=paquete1)
            comentario1.save()
            
            return redirect('AppAgregarAcompañantes')

        else:    
            messages.error(request, 'error del paquete')
            messages.error(request, mi_formulario.errors)
            messages.error(request, mi_formulario1.errors)
        
            return redirect('AppTurismoPaquete')
        
    
    context = {
        'form': PaqueteTuristicoFormulario(),
        'form1': ComentarioFormulario,
        'method': 'POST',
        'info':'LLenar Formulario',
        'title': 'PAQUETE TURISTICO',
        'Button_value': 'Enviar',
        
    }
    return render(request,'AppTurismo/formulario_universal.html', context)

@login_required
def agregar_acompañantes(request):
    
    context = {
        'title': 'AGREGAR ACOMPAÑANTE',
        
    }
    return render(request,'AppTurismo/agregar_acompañantes.html',context)



@login_required
def cliente (request):
    names = ['Messi', 'Cr7', 'Alberto', 'Mirta', 'Raul', 'Ibai']
    choice_name = random.choice(names)
    paquete= PaqueteTuristico.objects.last()

    
    if request.method == 'POST':
        formulario_cliente = ClienteFormulario(request.POST)
        
        if formulario_cliente.is_valid():
            data = formulario_cliente.cleaned_data
            try:
                cliente1 = Cliente(nombre= data.get('nombre'), apellido= data.get('apellido'),
                        email= data.get('email'), celular= data.get('celular'),
                        dni= data.get('dni'), empleado_asignado= choice_name, 
                        user=request.user)
           
                cliente1.save()
                paquete_acompanante = PaqueteAcompanante(user=request.user, paquete_turistico= paquete, cliente=cliente1)
                paquete_acompanante.save()

                messages.info(request, 'Se guardo su paquete de viaje')
                return redirect('AppInicio')
            except:
                messages.error(request, 'error del cliente')
                messages.error(request, cliente1.errors)
                return redirect('AppCliente')
    
    nombre_completo = f'{request.user.first_name} {request.user.last_name}'
    context = {
        'form': ClienteFormulario(),
        'method': 'POST',
        'title': 'FORMULARIO CLIENTE',
        'Button_value': 'Enviar',
        'info': nombre_completo,
        'info1': 'A quien deseas agregar como acompañante???'
        
    }
    
    return render(request, 'AppTurismo/formulario_universal.html', context)

@login_required
def busqueda_peticion_post (request):
    
    dni = request.GET.get('dni')
    cliente1 = Cliente.objects.filter(dni__exact=dni)
    idcliente = (cliente1)
    for id in idcliente:
        paquete_editar = PaqueteTuristico.objects.filter(id__exact=id.id)
    
    context = {
    'info1': paquete_editar,
    'info': cliente1,
    'title': 'BUSQUEDA CLIENTE',    
    }    
    return render(request, 'AppTurismo/busqueda_peticion_post.html', context)

@login_required
def busqueda_de_peticion(request):

    context = {
        'form': BusquedaPeticionFormulario(),
        'title': 'BUSQUEDA PETICIÓN',
        'Button_value': 'Buscar',
        
    }        
    
    return render(request, 'AppTurismo/busqueda_paquete.html', context)

@login_required
def elminar_peticion(request, dni):
    
    cliente_eliminar = Cliente.objects.get(dni=dni)
    cliente_eliminar.delete()
    messages.info(request, f'El Acompañante {cliente_eliminar} fue eliminado')
    
    return redirect('AppPaqueteContratado')

@login_required
def editar_cliente(request, dni):
        try:
            cliente_editar = Cliente.objects.get(dni=dni)
            id = cliente_editar.id
            paquete_editar = PaqueteTuristico(id=id)
            
            
            if request.method == 'POST':
                mi_formulario = ClienteFormulario(request.POST)
                mi_formulario1 = PaqueteTuristicoFormulario(request.POST)
                
                if mi_formulario.is_valid() and mi_formulario1.is_valid():
                    data = mi_formulario.cleaned_data
                    data1 = mi_formulario1.cleaned_data
                    
                    cliente_editar.nombre = data.get('nombre')
                    cliente_editar.apellido = data.get('apellido')
                    cliente_editar.email = data.get('email')
                    cliente_editar.celular = data.get('celular')
                    cliente_editar.dni = data.get('dni')
                    cliente_editar.save()
                    
                    paquete_editar.lugares = data1.get('lugares')
                    paquete_editar.fecha_de_entrada = data1.get('fecha_de_entrada')
                    paquete_editar.fecha_de_salida = data1.get('fecha_de_salida')
                    paquete_editar.save()
                    
                    messages.info(request,'Se actualizo!')
                    return redirect('AppInicio')
            
                    
        except:    
            messages.info(request,'error, no se actualizo')
        
        
        context = {
            'title': 'EDITAR CLIENTE',
            'method': 'POST',
            'Button_value': 'Editar',
            'info': 'Modificar Paquete de viaje contratado:',
            'form': ClienteFormulario(
                initial= {
                    'dni': cliente_editar.dni,
                    'nombre': cliente_editar.nombre,
                    'apellido': cliente_editar.apellido,
                    'email': cliente_editar.email,
                    'celular': cliente_editar.celular,   
                }
            ),
            'form1': PaqueteTuristicoFormulario(
                initial={
                    'lugares': paquete_editar.lugares,
                    'fecha_de_entrada': paquete_editar.fecha_de_entrada,
                    'fecha_de_salida': paquete_editar.fecha_de_salida
                    
                }
            )
        }
    
        return render(request, 'AppTurismo/formulario_universal.html', context)
    
@login_required    
def eliminar_paquete(request, id):

    paquete_eliminar = PaqueteTuristico.objects.get(id=id)
    paquete_eliminar.delete()
    messages.info(request, f'El Paquete {paquete_eliminar} fue eliminado')
    
    return redirect ('AppPaqueteContratado')



@login_required
def paquete_contratado(request):
    
    paquetes = PaqueteTuristico.objects.filter(user=request.user)
    acompanantes = Cliente.objects.filter(user=request.user)
    context = {
        'info': paquetes,
        'info1': acompanantes,
    }
        
        
    return render(request,'AppTurismo/busqueda_peticion_post.html', context)
    
    