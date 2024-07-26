from django import forms


class NuevoDentista(forms.Form): # Creación de Clase NuevoDentista para registro de nuevos dentistas por formulario.
    nombre = forms.CharField(max_length=100)
    especialidad = forms.CharField(max_length=100)
    formacion = forms.CharField(max_length=100)
    planta = forms.BooleanField(required=False)

class BuscaDentista(forms.Form): # Creación de Clase BuscaDentista para busqueda de dentistas por barra de busqueda.
    nombre = forms.CharField(max_length=100)