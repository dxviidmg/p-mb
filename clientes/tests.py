from django.test import TestCase
from .models import Cliente
from rest_framework.test import APIClient

class ClienteModelTest(TestCase):
    def testrea_cte(self):
        cliente = Cliente.objects.create(codigo = 1, domicilio = "cdmx", nombre= "Ramon", tipo = 4)
        self.assertEquals(cliente.codigo, 1)

class ClienteAPITest(TestCase):
    def test_consulta(self):

        client = APIClient()
        response = client.get(
                '/clientes/', {},
            format='json'
        )
        self.assertEquals(response.status_code, 200)