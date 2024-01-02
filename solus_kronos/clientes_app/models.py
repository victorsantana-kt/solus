# clientes_app/models.py

from django.db import models
from django.conf import settings  # Importe as configurações
from django.conf import settings 

class ClienteApp(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)  # Assumindo que você queira manter o CNPJ aqui também    
    responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='clientes_responsaveis'
    )
    def __str__(self):
        return f"{self.nome} - {self.produto.nome}"
