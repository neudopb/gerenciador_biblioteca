from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import Usuario
from .serializers import UsuarioSerializer

class UsuarioCreateAPIView(generics.CreateAPIView):
    '''Cadastrar Usuario'''
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioListAPIView(generics.ListAPIView):
    '''Listar usuario'''
    permission_classes = (IsAuthenticated,)
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        return Usuario.objects.filter(email=self.request.user.email)