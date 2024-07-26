from django.db import models

class Dentista(models.Model): #Modelo Dentistas para sustentar acciones CRUD
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    formacion = models.CharField(max_length=100)
    planta = models.BooleanField(default=False)

    def __str__(self): #Metodo magico para visualizacion de registros por nombre en admin DJANGO.
        return self.nombre
