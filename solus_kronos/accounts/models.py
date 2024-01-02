from django.contrib.auth.models import AbstractUser
from django.db import models
from clientes_kronos.models import Cliente
from filiais.models import Filial  # Substitua <app_name> pelo nome do seu app que contém o modelo Filial

class CustomUser(AbstractUser):
    nome = models.CharField(max_length=100)
    dataCadastro = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=(
        ('ativado', 'Ativado'),
        ('desativado', 'Desativado'),
    ), default='ativado')
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='usuarios', null=True, blank=True)
    #cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='usuarios', null=True, blank=True, editable=False)

    filial = models.ForeignKey(Filial, on_delete=models.CASCADE, related_name='usuarios', null=True, blank=True)  # Nova relação com Filial

    def is_super_user(self):
        return self.is_superuser
