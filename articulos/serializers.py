from rest_framework import serializers
from .models import Articulo

class ArticuloSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Articulo
        fields = ("url", "codigo", "descripcion", "precio", "proveedores")