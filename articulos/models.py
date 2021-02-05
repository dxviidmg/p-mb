from django.db import models
from proveedores.models import Proveedor
from core.models import *

class Articulo(Tiempo):
    codigo = models.CharField(max_length=30, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    proveedores = models.ManyToManyField(Proveedor, related_name='articulo_proveedor')

    def __str__(self):
        return self.codigo + " " + self.descripcion
