from django.db import models
from django.utils import timezone
from accounts.models import Usuario

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Genero'

class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    coautor = models.CharField(max_length=50, blank=True)
    data_cadastro = models.DateField(default = timezone.now)
    emprestado = models.BooleanField(default=False)
    genero = models.ForeignKey(Genero, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Livro'

class Emprestimo(models.Model):
    data_emprestimo = models.DateTimeField(default= timezone.now)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.usuario} - {self.livro}"

    class Meta:
        verbose_name = 'Emprestimo'