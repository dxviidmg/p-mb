from django.shortcuts import render
from .models import Pedido
from rest_framework import viewsets
from .serializers import PedidoSerializer
from rest_framework.response import Response
from clientes.models import Cliente
#from core.utils import get_model_attributes
from django.db.models import Count

class PedidoViewSet(viewsets.ModelViewSet):
#    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def get_queryset(self):
        data = self.request.data
        keys = list(data.keys())

        if 'parametros_cliente' in keys and 'parametros_pedido' in keys:
            clientes = Cliente.objects.filter(**data['parametros_cliente'])
            pedidos = Pedido.objects.filter(**data['parametros_pedido']).filter(cliente__in=clientes)
            return pedidos
        return Pedido.objects.all()

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