from django.contrib import admin
from .models import NotaFiscal
from django.utils.html import format_html


@admin.register(NotaFiscal)
class NotaFiscalAdmin(admin.ModelAdmin):
    list_display = ('nome_fornecedor', 'cnpj_fornecedor', 'numero_nf', 'usuario_cadastrou', 'cliente_associado', 'data_cadastro')
    search_fields = ('nome_fornecedor', 'cnpj_fornecedor', 'numero_nf')
    list_filter = ('cliente_associado', 'data_cadastro')
    
    def arquivo_link(self, obj):
        if obj.get_arquivo_url():
            return format_html("<a href='{}'>Baixar Arquivo</a>", obj.get_arquivo_url())
        return "Nenhum arquivo"

    arquivo_link.short_description = 'Arquivo NF'
    list_display = ('nome_fornecedor', 'cnpj_fornecedor', 'numero_nf', 'usuario_cadastrou', 'cliente_associado', 'data_cadastro', 'arquivo_link')
    
