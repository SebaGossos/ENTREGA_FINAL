import re
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from AppUser.models import Comentario
from AppTurismo.forms import *
from AppTurismo.models import *
from AppTurismo.choices import choice_name
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
                                        fecha_de_salida=data.get('fecha_de_salida'), empleado_asignado = choice_name , user=request.user)
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

    paquete= PaqueteTuristico.objects.last()
    if request.method == 'POST':
        formulario_cliente = ClienteFormulario(request.POST)
        
        if formulario_cliente.is_valid():
            data = formulario_cliente.cleaned_data
            try:
                cliente1 = Cliente(nombre= data.get('nombre'), apellido= data.get('apellido'),
                        email= data.get('email'), celular= data.get('celular'),
                        dni= data.get('dni'), user=request.user)
                
                cliente1.save()

                paquete_acompanante1 = PaqueteAcompanante(user=request.user, paquete_turistico= paquete, cliente=cliente1)
                paquete_acompanante1.save()

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
def eliminar_paquete(request, id, dni):
    cliente_eliminar = Cliente.objects.get(dni=dni)
    cliente_eliminar.delete()
    
    paquete = PaqueteTuristico.objects.get(id=id)
    paquete.delete()
    
    messages.info(request, f'El Paquete {paquete} fue eliminado')
    
    return redirect ('AppPaqueteContratado')

# def editar_paquete(request,):
    

@login_required
def paquete_contratado(request):
    
    paquetes = PaqueteTuristico.objects.filter(user=request.user)
    acompanantes = Cliente.objects.filter(user=request.user)

    context = {
        'info': paquetes,
        'info1': acompanantes,    
    }
        
    return render(request,'AppTurismo/busqueda_peticion_post.html', context)

def politica_de_privacidad(request):
    
    context = {
        'info': 'El usuario otorga su consentimiento informado de las siguientes cuestiones: El acceso a la información del usuario queda restringido al propio usuario mediante el uso de su “palabra clave” o contraseña. Coderhouse se reserva el derecho de compartir los datos necesarios con entidades relacionadas con los temas aprendidos, por ejemplo en el marco de búsquedas laborales, teniendo en cuenta el mejor interés de los estudiantes. Coderhouse no venderá ningún tipo de información a entidades externas ni utilizará datos de los estudiantes con fines publicitarios. Únicamente utilizará datos con fines educativos  autorizados. Para una mejor comprensión, ver la Política de Protección de Datos Personales que lleva a cabo Coderhouse.'
    }
    return render(request,'base/politicas_de_privacidad.html', context)

def acerca_de_mi(request):
    
    context = {
        'info': 'Hola a la persona que este corrigiendo este proyecto. Honestamente, estoy super agradecido con coder house por permitirme conocer un poco de lo que es ser un programador. se que mi web no es la mejor pero estoy orgulloso de mi por conseguir todo esto, empezando desde 0 con este curso de python, me queda mucho por aprender como html, css, base de datos(que de eso solo se lo que el profe explico en clase y me la he pasado viendo explicaciones en youtube de como conectar los models entre si XD.), etx. me inscribi a la carrera de full stack en coder y recien estoy empezando. Me gustaría aclarar que intente hacer este proyecto con mi compañero asignado, tuve comunicacion con el al pricipio pero despues desaparecio y no me contesto mas. lo hice solo y como pude reviendo las clases del profe y buscando info por otros lugares. Bueno como dije al principio estoy absolutamente agradecido.  Nos vemos en la proxima y bendiciones! ' 
    }
    return render(request,'base/politicas_de_privacidad.html', context)
    
    