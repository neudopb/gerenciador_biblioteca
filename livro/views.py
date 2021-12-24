from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from livro.models import Genero, Livros
from livro.serializers import GeneroSerializer, LivrosSerializer

class LivrosListCreateAPIView(ListCreateAPIView):
    '''Cadastrar e listar Livros'''
    permission_classes = (IsAuthenticated,)
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer

class LivrosRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    '''Detalhar, editar e excluir Livros'''
    permission_classes = (IsAuthenticated,)
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer

class GeneroListCreateAPIView(ListCreateAPIView):
    '''Cadastrar e listar Genero'''
    permission_classes = (IsAuthenticated,)
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer  

class GeneroRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    '''Detalhar, editar e excluir Genero'''
    permission_classes = (IsAuthenticated,)
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer