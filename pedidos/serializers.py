from rest_framework import serializers
from .models import Destino, Pedido

class DestinoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Destino
        fields = ("url", "cliente", "tipo", "almacen", "referencia", "codigo_sucursal", "codigo_socio", "detalle")

class PedidoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pedido
        fields = ("url", "numero", "articulo", "cliente", "surtido", "es_urgente", "destino", "cantidad")



