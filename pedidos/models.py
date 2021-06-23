from django.db import models
from proveedores.models import Tiempo
from articulos.models import *
from clientes.models import *
from proveedores.validators import validacion_alfanumerica

class Destino(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = ((1, 'Centro de distribución'), (2, 'Sucursal'), (3, 'Empresa asociada'))
    #Destino Centro de distribución
    almacen = models.CharField(max_length=30, null=True, blank=True, validators=[validacion_alfanumerica])

    #Destino Sucursal o Empresa asociada
    referencia = models.CharField(max_length=30, null=True, blank=True, validators=[validacion_alfanumerica])    

    #Destino Sucursal
    codigo_sucursal = models.IntegerField(null=True, blank=True)

    #Destino Empresa asociada
    codigo_socio = models.IntegerField(null=True, blank=True)
    detalle = models.CharField(max_length=30, null=True, blank=True)

class Pedido(Tiempo):
    numero = models.IntegerField()
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    surtido = models.DateTimeField(null=True, blank=True)
    es_urgente = models.BooleanField(default=False)
    cantidad = models.IntegerField()

    def __str__(self):
        return "No. " + str(self.id)

