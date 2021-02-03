from django.db import models
from core.models import *

class Proveedor(Tiempo, Entidad):
    
    def __str__(self):
        return self.nombre