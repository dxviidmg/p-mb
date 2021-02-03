from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.TextField()

    def __str__(self):
        return self.nombre