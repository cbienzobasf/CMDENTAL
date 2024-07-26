from django import forms

class BuscaEspecialidad(forms.Form):
    especialidad = forms.CharField(max_length=100)

class NuevaEspecialidad(forms.Form):
    especialidad = forms.CharField(max_length=100)
    disponible = forms.BooleanField(required=False)
    