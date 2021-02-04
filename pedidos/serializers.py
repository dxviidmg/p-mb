from rest_framework import serializers
from .models import Pedido

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = ("id", "articulo", "cliente", "surtido", "es_urgente", "destino", "cantidad", "almacen", "referencia", "codigo_sucursal", "codigo_socio", "detalle")

    def create(self, validated_data):
        data = self.context['request'].data
        keys = data.keys()
        destino = data['destino']
        if destino == 1:
            if not 'almacen' in keys:
                raise serializers.ValidationError("Incluir el almacen")
            
            atributos_sobrantes = ','.join(set(["referencia", "codigo_sucursal", "codigo_socio", "detalle"]).intersection(keys))

            if atributos_sobrantes != '':
                raise serializers.ValidationError("Borrar los atributos: " + atributos_sobrantes)

        elif destino == 2:
            if not 'referencia' in keys:
                raise serializers.ValidationError("Incluir el referencia")

            if not 'codigo_sucursal' in keys:
                raise serializers.ValidationError("Incluir el codigo_sucursal")

            atributos_sobrantes = ','.join(set(["almacen", "codigo_socio", "detalle"]).intersection(keys))

            if atributos_sobrantes != '':
                raise serializers.ValidationError("Borrar los atributos: " + atributos_sobrantes)

        elif destino == 3:
            if not 'referencia' in keys:
                raise serializers.ValidationError("Incluir el referencia")

            if not 'codigo_socio' in keys:
                raise serializers.ValidationError("Incluir el codigo_socio")

            if not 'detalle' in keys:
                raise serializers.ValidationError("Incluir el detalle")

            atributos_sobrantes = ','.join(set(["almacen", "codigo_sucursal"]).intersection(keys))

            if atributos_sobrantes != '':
                raise serializers.ValidationError("Borrar los atributos: " + atributos_sobrantes)

        pedido = Pedido.objects.create(**validated_data)
        return pedido