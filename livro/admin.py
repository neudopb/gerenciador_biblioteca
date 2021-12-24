from django.contrib import admin
from .models import Livros, Genero, Emprestimo

admin.site.register(Livros)
admin.site.register(Genero)
admin.site.register(Emprestimo)