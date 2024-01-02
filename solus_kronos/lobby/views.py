from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AbstractUser
from produtos.models import Produto, ClienteProduto



@login_required
def lobby(request):
    user = request.user
    cliente = user.cliente

    # Verifica se o cliente está associado ao produto_id=3
    #if ClienteProduto.objects.filter(cliente=cliente, produto_id=10).exists():
    #   return render(request, 'avaliacoes/formulario_avaliacao.html')
    #else:
    return render(request, 'lobby/lobby.html')
    


@login_required
def index(request):
    return render(request, 'lobby/index.html')


