from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.models import Usuario
from emprestimo.models import Emprestimo
from emprestimo.serializers import EmprestimoSerializer
from livro.models import Livros

class EmprestimoListCreateAPIView(ListCreateAPIView):
    '''Cadastrar e listar emprestimos'''
    permission_classes = (IsAuthenticated,)
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

    def create(self, request, *args, **kwargs):
        emprestimo = request.data

        if not emprestimo.get('usuario'):
            emprestimo['usuario'] = self.request.user
        elif self.request.user.id != emprestimo['usuario'] and self.request.user.is_superuser == False:
            emprestimo['usuario'] = self.request.user
        else:
            emprestimo['usuario'] = Usuario.objects.get(id=emprestimo['usuario'])

        livro = Livros.objects.get(id=emprestimo['livro'])
        
        if livro.emprestado:
            return Response({"message": "Livro emprestado"})

        if emprestimo.get('devolvido'):
            livro.emprestado = False
        else:
            livro.emprestado = True

        livro.save()

        new_emprestimo = Emprestimo.objects.create(
            data_emprestimo = emprestimo['data_emprestimo'],
            data_devolucao = emprestimo['data_devolucao'],
            livro = livro,
            usuario = emprestimo['usuario'],
        )
        serializer = EmprestimoSerializer(new_emprestimo)

        return Response(serializer.data)

class EmprestimoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    '''Detalhar, editar e excluir Emprestimo'''
    permission_classes = (IsAuthenticated,)
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

    def update(self, request, *args, **kwargs):
        try:
            emprestimo = self.get_object()

            if request.data.get('usuario'):
                if self.request.user.id != request.data.get('usuario') and self.request.user.is_superuser == False:
                    emprestimo.usuario = self.request.user
                else:
                    emprestimo.usuario = Usuario.objects.get(id=request.data['usuario'])
                
            if request.data.get('devolvido'):
                emprestimo.devolvido = request.data['devolvido']
                if emprestimo.devolvido and (not request.data.get('livro')):
                    livro = Livros.objects.get(id=emprestimo.livro.id)
                    livro.emprestado = False
                    livro.save()
                
            if request.data.get('livro'):
                livro = Livros.objects.get(id=request.data['livro'])

                if (not livro.emprestado) and (not emprestimo.devolvido):
                        livro.emprestado = False
                        livro.save()
                        emprestimo.livro = livro

            if request.data.get('data_emprestimo'):
                emprestimo.data_emprestimo = request.data.get('data_emprestimo')

            if request.data.get('data_devolucao'):
                emprestimo.data_devolucao = request.data.get('data_devolucao')

            resp = emprestimo.save()

            return Response(status=204)
        except:
            return Response(status=404)

class EmprestimoDevolver(ListAPIView):
    '''Finalizar demanda'''
    permission_classes = (IsAuthenticated, )
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

    def get_queryset(self):
        emprestimo = Emprestimo.objects.get(id=self.kwargs['pk'])
       
        if self.request.user.id == emprestimo.usuario.id or self.request.user.is_superuser == True:
            emprestimo.devolvido = True

            livro = Livros.objects.get(id=emprestimo.livro.id)
        
            livro.emprestado = False

            livro.save()
            emprestimo.save()
        
        return Emprestimo.objects.filter(id=emprestimo.id)