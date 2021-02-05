from django.shortcuts import render
from .models import Pedido
from rest_framework import viewsets
from .serializers import PedidoSerializer
from rest_framework.response import Response
from clientes.models import Cliente

class PedidoViewSet(viewsets.ModelViewSet):
#    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def get_queryset(self):
        data = self.request.data
        keys = data.keys()
        if 'parametros_cliente' in keys and 'parametros_pedido' in keys:
            clientes = Cliente.objects.filter(**data['parametros_cliente'])
            pedidos = Pedido.objects.filter(**data['parametros_pedido']).filter(cliente__in=clientes)
            return pedidos
        return Pedido.objects.all()