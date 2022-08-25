from pickle import TRUE
from django.db import models


class Personal(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    puesto = models.CharField(max_length=100, null=TRUE)
    fecha_nacimiento = models.DateField(blank=TRUE, null=TRUE)
    año_ingreso = models.IntegerField()

    def __str__(self):
        return f"{self.nombre.capitalize()} - {self.apellido.upper()} - {self.puesto}"