from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import NotaFiscal




class NotaFiscalForm(forms.ModelForm):
    class Meta:
        model = NotaFiscal
        fields = ['nome_fornecedor', 'cnpj_fornecedor', 'numero_nf', 'data_emissao_nf', 'descricao', 'arquivo_nf','boleto']
        widgets = {
            'nome_fornecedor': forms.TextInput(attrs={'type': 'text','class': 'form-control'}),
            'cnpj_fornecedor': forms.TextInput(attrs={'class': 'form-control','type': 'number'}),
            'numero_nf': forms.TextInput(attrs={'class': 'form-control','type': 'number'}),
            'data_emissao_nf': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            #'status_ssw': forms.Textarea(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'arquivo_nf': forms.FileInput(attrs={'accept': '.pdf, .doc, .docx, .jpg, .jpeg, .png', 'class': 'form-control'}),
            'boleto': forms.FileInput(attrs={'accept': '.pdf, .doc, .docx, .jpg, .jpeg, .png', 'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(NotaFiscalForm, self).__init__(*args, **kwargs)
        # Você pode adicionar mais atributos ou lógicas de inicialização aqui se necessário
        
class NotaFiscalFilterForm(forms.Form):
    nome_fornecedor = forms.CharField(required=False)
    cnpj_fornecedor = forms.CharField(required=False)
    numero_nf = forms.CharField(required=False)
    