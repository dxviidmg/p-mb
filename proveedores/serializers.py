from rest_framework import serializers
from .models import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):

    articulo_proveedor = serializers.StringRelatedField(many=True, read_only = True)

    class Meta:
        model = Proveedor
        fields = ("id", "nombre", "domicilio", "articulo_proveedor")