from django.contrib import admin # Importa el modulo admin de Django.

from .models import Dentista # Importa el modelo Dentista desde el modulo models.

admin.site.register(Dentista) # Registrar el modelo Dentista en el sitio administrativo de Django.