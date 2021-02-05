from rest_framework import serializers
from .models import Proveedor
from articulos.serializers import ArticuloSerializer

class ProveedorSerializer(serializers.HyperlinkedModelSerializer):
    articulo_proveedor = ArticuloSerializer(many=True, read_only = True)
    
    class Meta:
        model = Proveedor
        fields = ("url", "nombre", "domicilio", "articulo_proveedor")