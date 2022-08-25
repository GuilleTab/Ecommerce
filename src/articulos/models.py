from pickle import TRUE
from django.db import models

class Articulo(models.Model):

    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField()
    vencimiento = models.DateField(blank=TRUE, null=TRUE)

    def __str__(self):
        return f"{self.nombre} - {self.marca} - {self.precio}"
