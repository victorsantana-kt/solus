from django.db import models
from clientes_kronos.models import Cliente  # Importe o modelo Cliente

class Setor(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='setores')

    def __str__(self):
        return self.nome
