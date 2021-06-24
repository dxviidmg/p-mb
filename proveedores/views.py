from django.shortcuts import render
from .models import Proveedor
from rest_framework import viewsets
from .serializers import ProveedorSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
