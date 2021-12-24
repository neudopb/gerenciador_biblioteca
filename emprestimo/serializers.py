from rest_framework import serializers
from emprestimo.models import Emprestimo

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'