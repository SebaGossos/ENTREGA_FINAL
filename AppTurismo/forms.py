from django import forms
from AppUser.models import Comentario


class PaqueteTuristicoFormulario(forms.Form):
    
    lugares = forms.CharField(max_length= 33)
    fecha_de_entrada = forms.DateField()
    fecha_de_salida = forms.DateField()
    
    
class ComentarioFormulario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('comentario',)



class ClienteFormulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    celular = forms.IntegerField()
    dni = forms.IntegerField()
    
class BusquedaPeticionFormulario(forms.Form):
    dni = forms.IntegerField()
