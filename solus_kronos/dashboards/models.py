from django.db import models
from django.conf import settings
from clientes_kronos.models import Cliente  # Importe o modelo Cliente



class Dashboard(models.Model):
    AREA_CHOICES = [
        ('financeiro', 'Financeiro'),
        ('logistica', 'Logística'),
        ('comercial', 'Comercial'),
        ('operação', 'Operação'),
        ('outros', 'Outros'),
    ]

    nome = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='dashboards')
    area = models.CharField(max_length=50, choices=AREA_CHOICES)
    link = models.URLField()
    usuario_cadastrou = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
