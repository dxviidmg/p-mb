from django.db import models

class Tiempo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class Entidad(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.TextField()

    class Meta:
        abstract = True
