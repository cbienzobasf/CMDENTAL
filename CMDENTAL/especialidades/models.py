from django.db import models

class Especialidad(models.Model):
    especialidad = models.CharField(max_length=100)
    disponible = models.BooleanField(default=False)


    def __str__(self):
        return self.especialidad
