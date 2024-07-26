from django.db import models

class Sucursal(models.Model):
    clinica = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.FloatField(max_length=100)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return self.clinica
