from rest_framework import serializers
from livro.models import Genero, Livros, Emprestimo
from accounts.serializers import UsuarioSerializer

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class LivrosSerializer(serializers.ModelSerializer):
    genero = GeneroSerializer()

    class Meta:
        model = Livros
        fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    livro = LivrosSerializer()

    class Meta:
        model = Emprestimo
        fields = '__all__'