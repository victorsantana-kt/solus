from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from clientes_kronos.models import Cliente  # Importe o modelo Cliente
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from clientes_kronos.models import Cliente  # Importe o modelo Cliente


class CustomUserCreationForm(UserCreationForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'nome', 'status', 'cliente')  # Incluído 'cliente' nos campos


class CustomUserChangeForm(UserChangeForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=True)

    class Meta:
        model = get_user_model()
        fields = ('nome', 'username', 'email', 'cliente')  # Incluído 'cliente' nos campos
