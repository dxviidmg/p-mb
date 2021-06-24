from django.shortcuts import render
from .models import Articulo
from rest_framework import viewsets
from .serializers import ArticuloSerializer

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer