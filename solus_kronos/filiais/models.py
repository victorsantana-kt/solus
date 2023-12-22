from django.db import models
from clientes_kronos.models import Cliente  # Importando o modelo Cliente

class Filial(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10, unique=True)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    responsavel = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='filiais')  # Associando a Cliente

    def __str__(self):
        return self.nome
