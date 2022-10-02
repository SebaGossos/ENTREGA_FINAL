from django import forms
from AppUser.models import Comentario
from AppTurismo.models import PaqueteTuristico

class DateInput(forms.DateInput):
    input_type = 'date'
class PaqueteTuristicoFormulario(forms.ModelForm):
    
    class Meta:
        model = PaqueteTuristico
        fields = ['lugares','fecha_de_entrada','fecha_de_salida']
        widgets = {'fecha_de_entrada':DateInput(), 'fecha_de_salida':DateInput()}

    
    
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
