from rest_framework.serializers import ModelSerializer, CharField

from livraria.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ["livro", "quantidade"]
        depth = 2

class CompraSerializer(ModelSerializer):
    class Meta:
        usuario = CharField(source="usuario.email", read_only=True)
        status = CharField(source="get_status_display", read_only=True)
        model = Compra
        fields = "__all__"
        itens = ItensCompraSerializer(many=True, read_only=True)