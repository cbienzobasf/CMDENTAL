from django.shortcuts import render,redirect
from .models import Sucursal
from sucursales.forms import BuscarSucursal, NuevaSucursal
from django.contrib import messages


def sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursales/sucursales.html', {'sucursales': sucursales})

def buscar_sucursales(request):

    sucursales = None
    if request.method == "POST":
        inFormulario = BuscarSucursal(request.POST)

        if inFormulario.is_valid():
            informacion = inFormulario.cleaned_data
            sucursales = Sucursal.objects.filter(clinica__icontains=informacion["clinica"])

    else:
        inFormulario = BuscarSucursal()

    return render(request, "sucursales/buscar_sucursales.html", {"inFormulario": inFormulario, "sucursales": sucursales})

def agregar_sucursales(request):
    if request.method == "POST":
        on_formulario = NuevaSucursal(request.POST) 
        if on_formulario.is_valid():
            informacion = on_formulario.cleaned_data
            
            sucursal = Sucursal(clinica=informacion["clinica"], direccion=informacion["direccion"], telefono=informacion["telefono"], horario=informacion["horario"])
            sucursal.save()
            messages.success(request, 'sucursal agregada exitosamente!')

            return redirect("agregar sucursales")
    else:
        on_formulario = NuevaSucursal()

    return render(request, "sucursales/agregar_sucursales.html", {"on_formulario": on_formulario})