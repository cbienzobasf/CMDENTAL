from django.shortcuts import render, redirect # import funciones render y redirect para actualizacion paginas al termino de accion. Nota: Se usa render por mejores resultados en refresh post
from dentistas.forms import NuevoDentista , BuscaDentista # import forms de add y search
from dentistas.models import Dentista #import modelo base
from django.contrib import messages #import para gestionar mensajes de exito en operaciones de vista.

def add_dentista(request): #Vista para agregar Dentistas
    if request.method == "POST": # metodo POST
        mi_formulario = NuevoDentista(request.POST) #instancia con los datos entregados
        if mi_formulario.is_valid(): # Si el formulario es valido entonces:
            informacion = mi_formulario.cleaned_data #obtiene los datos ya validados
            
            dentista = Dentista(nombre=informacion["nombre"], especialidad=informacion["especialidad"],formacion=informacion["formacion"], planta=informacion["planta"]) #guarda informacion ya validada en la Base de datos a traves de una nueva instancia.
            dentista.save()
            messages.success(request, 'Dentista agregado exitosamente!') # Entrega mensaje de exito de registro a reflejar en el FRONT.

            return redirect("agregar dentista") # Redirige al usuario a la misma vista para agregar otro dentista. AQUI SE USA REDIRECT porque render generaba errores visuales al momento de recargar el sitio.
    else:
        mi_formulario = NuevoDentista() # Establece instancia vacia del formulario si la solicitud no es POST.

    return render(request, "dentistas/agregar_dentista.html", {"mi_formulario": mi_formulario})# Renderiza la plantilla HTML y pasa el formulario como contexto. Bajo esta condiciones RENDER funciona segun lo esperado.

def search_dentista(request): #Vista para buscar Dentistas
    dentistas =None # Se define variable dentistas a None para almacenar los resultados de la búsqueda más tarde.
    if request.method == "POST": # Valida que sea un metodo POST.
        miFormulario = BuscaDentista(request.POST) # Crea instancia con los datos de busqueda entregados.

        if miFormulario.is_valid(): # Si el formulario es valido entonces:
            informacion = miFormulario.cleaned_data # Obtiene los datos validados del formulario.
            
            dentistas = Dentista.objects.filter(nombre__icontains=informacion["nombre"]) #busqueda en base de datos sobre campo "nombre" de registros ingresados en cuadro de busqueda.
            
            return render(request, "dentistas/buscar_dentista.html", {"miFormulario": miFormulario, "dentistas": dentistas}) # Renderiza la plantilla HTML para mostrar los resultados
    else:
        miFormulario = BuscaDentista() #Establece instancia vacia del formulario si la solicitud no es POST. 

    return render(request, "dentistas/buscar_dentista.html", {"miFormulario": miFormulario, "dentistas": dentistas}) # Renderiza la plantilla HTML y pasa el formulario como contexto. Bajo esta condiciones RENDER funciona segun lo esperado. 

def nuestros_dentistas(request): # Vista para visualizacion de dentistas de planta
    dentistas_planta = Dentista.objects.filter(planta=True) # Consulta a la base de datos para obtener todos los dentistas que son de planta, es decir con el campo "planta" como TRUE.
    return render(request, "dentistas/nuestros_dentistas.html", {"dentistas_planta": dentistas_planta}) # Renderiza la plantilla HTML, pasando la lista de dentistas de planta como contexto.