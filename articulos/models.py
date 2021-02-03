from django.db import models
from proveedores.models import Proveedor

class Articulo(models.Model):
    proveedor = models.ManyToManyField(Proveedor)
    codigo = models.CharField(max_length=30)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=20, decimal_places=2)