from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Autor, Categoria, Editora, Livro
from livraria.serializers.livro import (
    LivroDetailSerializer,
    LivroListSerializer,
    LivroSerializer,
)

# from rest_framework.permissions import IsAuthenticated


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer
