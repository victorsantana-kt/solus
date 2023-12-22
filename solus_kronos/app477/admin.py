from django.contrib import admin
from .models import Bd477

@admin.register(Bd477)
class Bd477Admin(admin.ModelAdmin):
    list_display = ['NUMLANCTO', 'EVENTO', 'DESCR_EVENTO', 'CNPJ_FORNECEDOR', 'NOME_FORNECEDOR']  # Personalize conforme necessário
    search_fields = ['NUMLANCTO', 'NOME_FORNECEDOR']  # Personalize conforme necessário
    # Adicione mais configurações conforme necessário
