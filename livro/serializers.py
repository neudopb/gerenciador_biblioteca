from rest_framework import serializers
from livro.models import Genero, Livros
from accounts.serializers import UsuarioSerializer

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = '__all__'