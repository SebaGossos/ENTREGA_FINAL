from django import forms


class PaqueteTuristicoFormulario(forms.Form):
    
    lugares = forms.CharField(max_length= 33)
    fecha_de_entrada = forms.DateField()
    fecha_de_salida = forms.DateField()
    

class ClienteFormulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    celular = forms.IntegerField()
    dni = forms.IntegerField()
    
class BusquedaPeticionFormulario(forms.Form):
    dni = forms.IntegerField()
