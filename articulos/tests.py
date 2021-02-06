from django.test import TestCase
from .models import Articulo
from rest_framework.test import APIClient

class ArticuloModelTest(TestCase):
    def test_create(self):
        articulo = Articulo.objects.create(codigo = 1, descripcion = "test", precio = 10)
        self.assertEquals(articulo.codigo, 1)

class ArticuloAPITest(TestCase):
    def test_consulta(self):

        client = APIClient()
        response = client.get(
                '/articulos/', {},
            format='json'
        )
        self.assertEquals(response.status_code, 200)