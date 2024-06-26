from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido

    class Meta:
        ordering = ['id']


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='proveedor')

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['id']
