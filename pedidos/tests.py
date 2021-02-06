from django.test import TestCase
from .models import Pedido
from articulos.models import Articulo
from pedidos.models import Cliente
from rest_framework.test import APIClient

class PedidoModelTest(TestCase):
    def test_create(self):
        articulo, articulo_created = Articulo.objects.get_or_create(codigo = 1, descripcion = "test", precio = 10)
        cliente, articulo_created = Cliente.objects.get_or_create(codigo = 1, domicilio = "cdmx", nombre= "Ramon", tipo = 4)

        data = {
            "articulo": articulo,
            "cliente": cliente,
            "es_urgente": True,
            "destino": 1,
            "cantidad": 2,
            "almacen": 1
        }
        pedido = Pedido.objects.create(**data)

        self.assertEquals(pedido.cantidad, 2)

class PedidoAPITest(TestCase):
    def test_consulta(self):

        client = APIClient()
        response = client.get(
                '/pedidos/', {},
            format='json'
        )
        self.assertEquals(response.status_code, 200)