from django.contrib import admin
from .models import Filial

@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'cidade', 'uf', 'responsavel', 'cliente')
    # Mais configurações conforme necessário
