from django.test import TestCase
from .models import Proveedor

class ProveedorModelTest(TestCase):
    def test_create(self):
        articulo = Proveedor.objects.create(nombre="test", domicilio = "test")
        self.assertEquals(articulo.nombre, "test")