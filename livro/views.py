from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from livro.models import Genero
from livro.serializers import GeneroSerializer

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