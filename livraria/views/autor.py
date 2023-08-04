from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Autor
from livraria.serializers import AutorSerializer

# from rest_framework.permissions import IsAuthenticated


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
