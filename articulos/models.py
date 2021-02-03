from django.db import models
from proveedores.models import Proveedor
from core.models import *

class Articulo(Tiempo):
    codigo = models.CharField(max_length=30)
    descripcion = models.TextField()

class ProveedorArticulo(Tiempo):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=20, decimal_places=2)