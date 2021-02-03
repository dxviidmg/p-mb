from rest_framework import serializers
from .models import Pedido

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ("id", "articulo", "cliente ", "surtido ", "es_urgente", "destino ", "cantidad", "almacen", "referencia", "codigo_sucursal", "codigo_socio", "detalle")