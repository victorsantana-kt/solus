
from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['descricao', 'status', 'responsavel', 'prazo', 'area']  # Sem 'cliente_kronos'