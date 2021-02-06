from django.test import TestCase
from .models import Articulo

class ArticuloModelTest(TestCase):
    def test_create(self):
        articulo = Articulo.objects.create(codigo = 1, descripcion = "test", precio = 10)
        self.assertEquals(articulo.codigo, 1)