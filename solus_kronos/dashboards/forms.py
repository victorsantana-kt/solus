from django import forms
from .models import Dashboard

class DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        exclude = ['usuario_cadastrou']  # Exclui o campo do formulário
