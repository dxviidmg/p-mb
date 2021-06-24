from django.test import TestCase
from .models import Proveedor
from rest_framework.test import APIClient

data = {
    "nombre": "test",
    "domicilio": "cmdx"
}
class ProveedorModelTest(TestCase):
    def test_create(self):
        articulo = Proveedor.objects.create(**data)
        self.assertEquals(articulo.nombre, "test")

class ProveedorAPITest(TestCase):
    def test_consulta(self):

        client = APIClient()
        response = client.get(
                '/proveedores/', {},
            format='json'
        )
        self.assertEquals(response.status_code, 200)

    def test_create(self):
        payload = {
            "nombre": "Fabrica",
            "domicilio": "cmdx"
            }
        headers = {
            'Content-Type': 'application/json'
        }

        client = APIClient()
        response = client.post(
                '/proveedores/', payload,
            format='json'
        )
        self.assertEquals(response.status_code, 201)
