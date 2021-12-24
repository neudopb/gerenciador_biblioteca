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
    data_cadastro = models.DateTimeField(default=timezone.now)
    emprestado = models.BooleanField(default=False)
    genero = models.ForeignKey(Genero, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Livro'