from django.db import models
from proveedores.models import Tiempo, Entidad

class Cliente(Tiempo, Entidad):
    tipo_choices = ((1, 'Normal'), (2, 'Plata'), (3, 'Oro'), (4, 'Platino'))
    codigo = models.CharField(max_length=30, unique=True)
    tipo = models.IntegerField(default=1, choices = tipo_choices)
    fotografia = models.ImageField(upload_to ='fotografias/%Y/%m/%d/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre
