from django.test import TestCase
from .models import Pedido, Destino
from articulos.models import Articulo
from clientes.models import Cliente
from rest_framework.test import APIClient

class DestinoModelTest(TestCase):
    def test_create(self):
        cliente, articulo_created = Cliente.objects.get_or_create(codigo = 1, domicilio = "cdmx", nombre= "Ramon", tipo = 4)

        data = {
            "cliente": cliente,
            "tipo": 1,
            "almacen": "Mi almacen"
        }
        destino = Destino.objects.create(**data)

        self.assertEquals(destino.pk, 1)

class DestinoAPITest(TestCase):
    def test_consulta(self):

        client = APIClient()
        response = client.get(
                '/destinos/', {},
            format='json'
        )
        self.assertEquals(response.status_code, 200)


class PedidoModelTest(TestCase):
    def test_create(self):
        articulo, articulo_created = Articulo.objects.get_or_create(codigo = 1, descripcion = "test", precio = 10)
        cliente, articulo_created = Cliente.objects.get_or_create(codigo = 1, domicilio = "cdmx", nombre= "Ramon", tipo = 4)
        destino, destino_created = Destino.objects.get_or_create(cliente=cliente, tipo= 1, almacen="Mi almacen")

        data = {
            "numero": 1,
            "articulo": articulo,
            "cliente": cliente,
            "es_urgente": True,
            "destino": destino,
            "cantidad": 2,
        }
        pedido = Pedido.objects.create(**data)

        self.assertEquals(pedido.cantidad, 2)


class DashboardAPITest(TestCase):
    def test_consulta(self):

        client = APIClient()
        response = client.get(
                '/dashboard/', {},
            format='json'
        )
        self.assertEquals(response.status_code, 200)