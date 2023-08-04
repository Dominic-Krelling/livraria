from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Editora
from livraria.serializers import EditoraSerializer

# from rest_framework.permissions import IsAuthenticated


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
