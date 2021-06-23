from django.db import models
from proveedores.models import Tiempo, Proveedor
from proveedores.validators import validacion_alfanumerica


class Articulo(Tiempo):
    codigo = models.CharField(max_length=30, unique=True)
    descripcion = models.TextField(validators=[validacion_alfanumerica])
    precio = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    proveedores = models.ManyToManyField(Proveedor, related_name='articulo_proveedor', null=True, blank=True)

    def __str__(self):
        return str(self.codigo) + " " + (self.descripcion)
