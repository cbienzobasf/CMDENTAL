
from django import forms

class BuscarSucursal(forms.Form):
    clinica = forms.CharField(max_length=100)

class NuevaSucursal(forms.Form):
    clinica = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=100)
    horario = forms.CharField(max_length=100)