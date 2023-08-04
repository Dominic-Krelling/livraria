from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria
from livraria.serializers import CategoriaSerializer

# from rest_framework.permissions import IsAuthenticated


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    # permission_classes = [IsAuthenticated]
