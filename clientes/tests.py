from django.test import TestCase
from .models import Cliente

class ClienteModelTest(TestCase):
    def test_create(self):
        cliente = Cliente.objects.create(codigo = 1, domicilio = "cdmx", nombre= "Ramon", tipo = 4)
        self.assertEquals(cliente.codigo, 1)