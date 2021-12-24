from django.db import models
from django.utils import timezone
from accounts.models import Usuario
from livro.models import Livros

class Emprestimo(models.Model):
    data_emprestimo = models.DateTimeField(default= timezone.now)
    data_devolucao = models.DateTimeField(blank=True,null=True)
    devolvido = models.BooleanField(default=False)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)


    def __str__(self):
        return f"{self.usuario} - {self.livro}"

    class Meta:
        verbose_name = 'Emprestimo'