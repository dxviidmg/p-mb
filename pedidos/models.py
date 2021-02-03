from django.db import models
from core.models import *
from articulos.models import *
from clientes.models import *

class Pedido(Tiempo):
    destino_choices = ((1, 'Centro de distribución'), (2, 'Sucursal'), (3, 'Empresa asociada'))

    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    surtido = models.DateTimeField(null=True, blank=True)
    es_urgente = models.BooleanField(default=False)
    destino = models.IntegerField(choices = destino_choices)
    cantidad = models.IntegerField()

    def __str__(self):
        return "No. " + str(self.id)