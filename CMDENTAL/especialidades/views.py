from django.shortcuts import render, redirect
from especialidades.forms import BuscaEspecialidad, NuevaEspecialidad
from especialidades.models import Especialidad
from django.contrib import messages

def especialidades(request):
    especialidades = Especialidad.objects.filter(disponible=True)
    return render(request, 'especialidades/especialidades.html', {'especialidades': especialidades})


def buscar_especialidades(request):
    especialidades = None
    if request.method == "POST":
        elFormulario = BuscaEspecialidad(request.POST)

        if elFormulario.is_valid():
            informacion = elFormulario.cleaned_data
            especialidades = Especialidad.objects.filter(especialidad__icontains=informacion["especialidad"])

    else:
        elFormulario = BuscaEspecialidad()

    return render(request, "especialidades/buscar_especialidades.html", {"elFormulario": elFormulario, "especialidades": especialidades})

def agregar_especialidades(request):
    if request.method == "POST":
        la_formulario = NuevaEspecialidad(request.POST) 
        # print(laFormulario)
        if la_formulario.is_valid():
            informacion = la_formulario.cleaned_data
            
            especialidad = Especialidad(especialidad=informacion["especialidad"], disponible=informacion["disponible"])
            especialidad.save()
            messages.success(request, 'Especialidad agregada exitosamente!')

            return redirect("agregar especialidades")
    else:
        la_formulario = NuevaEspecialidad()

    return render(request, "especialidades/agregar_especialidades.html", {"la_formulario": la_formulario})

