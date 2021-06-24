from django.shortcuts import render
from .models import Destino, Pedido
from rest_framework import viewsets, serializers, status
from .serializers import PedidoSerializer, DestinoSerializer
from rest_framework.response import Response
from clientes.models import Cliente
from django.db.models import Count
#from rest_framework import serializers
#from rest_framework import generics, status

class DestinoViewSet(viewsets.ModelViewSet):
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer

    def create(self, request):
        data = request.data
        print(data)
        keys = data.keys()
        tipo = int(data['tipo'])

#        import pdb; pdb.set_trace()

        if tipo == 1:
            if data['almacen'] == '':
                raise serializers.ValidationError("Incluir el almacen")
            
        elif tipo == 2:
            if data['referencia'] == '':
                raise serializers.ValidationError("Incluir el referencia")

            if data['codigo_sucursal'] == '':
                raise serializers.ValidationError("Incluir el codigo_sucursal")

        elif tipo == 3:
            if data['referencia'] == '':            
                raise serializers.ValidationError("Incluir el referencia")
            if data['codigo_socio'] == '':
                raise serializers.ValidationError("Incluir el codigo_socio")
            if data['detalle'] == '':
                raise serializers.ValidationError("Incluir el detalle")

        serializer = DestinoSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(data, status=status.HTTP_400_BAD_REQUEST)

class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer

    def get_queryset(self):
        data = self.request.data
        keys = list(data.keys())

        if 'parametros_cliente' in keys:
            clientes = Cliente.objects.filter(**data['parametros_cliente'])
        else:
            clientes = Cliente.objects.all()

        if 'parametros_destino' in keys:
            destinos = Destino.objects.filter(**data['parametros_destino'])
        else:
            destinos = Destino.objects.all()

        if 'parametros_pedido' in keys:
            pedidos = Pedido.objects.filter(**data['parametros_pedido']).filter(cliente__in=clientes, destino__in=destinos)
            return pedidos

        return Pedido.objects.all()


    def create(self, request):
        data = request.data
        id_destino = data['destino'].split('/')[-2]
        destino = Destino.objects.get(id=id_destino)
        id_cliente = int(data['cliente'].split('/')[-2])

        if destino.cliente.pk != id_cliente:
            raise serializers.ValidationError("Domicilio no corresponde a cliente")

        serializer = PedidoSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(data, status=status.HTTP_400_BAD_REQUEST)
            


class DashboardViewSet(viewsets.ViewSet):
    def list(self, request, format=None):
        pedidos_pendientes_urgentes = Pedido.objects.filter(surtido=None).values('es_urgente').annotate(Count('es_urgente'))
        pedidos_por_destino = Pedido.objects.values('destino').annotate(Count('destino'))
        pedidos_por_creacion = Pedido.objects.values('creado__date').annotate(Count('creado__date'))
        pedidos_por_surtido = Pedido.objects.exclude(surtido=None).values('surtido__date').annotate(Count('surtido__date'))
        clientes_por_tipo = Cliente.objects.values('tipo').annotate(Count('tipo'))

        content = {
            'pedidos_pendientes': pedidos_pendientes_urgentes,
            'pedidos_por_destino': pedidos_por_destino,
            'pedidos_por_creación': pedidos_por_creacion,
            'pedidos_por_surtido': pedidos_por_surtido,
            'clientes_por_tipo': clientes_por_tipo
        }
        return Response(content)