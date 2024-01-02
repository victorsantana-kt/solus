# clientes_app/forms.py

from django import forms
from .models import ClienteApp

class ClienteAppForm(forms.ModelForm):
    class Meta:
        model = ClienteApp
        fields = ['nome', 'cnpj']  # Inclua todos os campos que você quer no formulário
