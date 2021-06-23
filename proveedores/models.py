from django.db import models
from .validators import validacion_alfanumerica

class Tiempo(models.Model):
    creado = models.DateTimeField(auto_now_add=True, null=True)
    actualizado = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        

class Entidad(models.Model):
    nombre = models.CharField(max_length=30, validators=[validacion_alfanumerica])
    domicilio = models.TextField(validators=[validacion_alfanumerica])

    class Meta:
        abstract = True

class Proveedor(Tiempo, Entidad):
    
    def __str__(self):
        return self.nombre