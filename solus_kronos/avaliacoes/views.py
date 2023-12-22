from django.shortcuts import render, get_object_or_404
from .models import Avaliacao, Cliente
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required
def exibir_formulario_avaliacao(request):
    # Obtendo o cliente associado ao usuário logado
    cliente = request.user.cliente

    if cliente is None:
        # Tratamento para caso o usuário não tenha um cliente associado
        # Pode ser um redirecionamento ou uma mensagem de erro
        return render(request, 'avaliacoes/erro.html', {'mensagem': 'Usuário sem cliente associado.'})

    return render(request, 'avaliacoes/formulario_avaliacao.html', {'cliente': cliente})

@login_required
def submeter_avaliacao(request):
    if request.method == 'POST':
        cliente = request.user.cliente
        nivel_satisfacao = request.POST.get('nivel_satisfacao')

        if cliente is None:
            # Tratamento para caso o usuário não tenha um cliente associado
            # Pode ser um redirecionamento ou uma mensagem de erro
            return render(request, 'avaliacoes/erro.html', {'mensagem': 'Usuário sem cliente associado.'})

        try:
            Avaliacao.objects.create(
                cliente=cliente,
                usuario=request.user,
                unidade=request.user.filial,  # Atribuindo a filial do usuário logado
                nivel_satisfacao=nivel_satisfacao
            )
            return HttpResponseRedirect(reverse('avaliacao_sucesso'))  # Redireciona para uma página de sucesso
        except Exception as e:
            print(f"Erro ao salvar a avaliação: {e}")
            # Aqui você pode adicionar algum tratamento de erro ou redirecionamento

    return HttpResponseRedirect(reverse('avaliacao_sucesso'))


def agradecimento(request):
    return render(request, 'avaliacoes/agradecimento.html')
