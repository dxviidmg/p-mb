from django.test import TestCase
from .models import Cliente
from rest_framework.test import APIClient

class ClienteModelTest(TestCase):
    def test_create(self):
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

    def test_create(self):
        payload={"codigo": 3, "domicilio": "cdmx", "nombre": "dav", "tipo": 4}
        headers = {
            'Content-Type': 'application/json'
        }

        client = APIClient()
        response = client.post(
                '/clientes/', payload,
            format='json'
        )
        self.assertEquals(response.status_code, 201)