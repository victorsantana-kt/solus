from django.db import models
from django.conf import settings
from clientes_kronos.models import Cliente

class Avaliacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    unidade = models.CharField(max_length=100)
    nivel_satisfacao = models.IntegerField(choices=[(1, 'Muito Ruim'), (2, 'Ruim'), (3, 'Neutro'), (4, 'Bom'), (5, 'Excelente')])
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nivel_satisfacao} - {self.cliente.nome_empresa}'
