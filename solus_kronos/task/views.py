from django.shortcuts import render, get_object_or_404
from .models import Tarefa
from django.shortcuts import render, redirect
from .forms import TarefaForm
from django.contrib import messages
from produtos.models import Produto, ClienteProduto
from django.contrib.auth.decorators import login_required
from clientes_app.forms import ClienteAppForm
from clientes_app.models import ClienteApp

def cadastrar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa cadastrada com sucesso!')
            return redirect('lista_tarefas')  # Redireciona para a lista de tarefas após o cadastro
    else:
        form = TarefaForm()
        
    if request.method == 'POST':
        formClientes = ClienteAppForm(request.POST)
        if formClientes.is_valid():
            formClientes.save()
            return redirect('lista_tarefas')  # Redireciona para a view de lista após o cadastro
    else:
        formClientes = ClienteAppForm()    

    return render(request, 'task/lista_tarefas.html', {'form': form,'formClientes': formClientes})


@login_required
def lista_tarefas(request):
    try:
        produto_dashboard_acesso = Produto.objects.get(nome='Task')
        if not ClienteProduto.objects.filter(cliente=request.user.cliente, produto=produto_dashboard_acesso).exists():
            return render(request, 'lobby/acesso_proibido.html')
    except Produto.DoesNotExist:
        return render(request, 'lobby/acesso_proibido.html')
    
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            nova_tarefa = form.save(commit=False)
            if not nova_tarefa.cliente_kronos:
                nova_tarefa.cliente_kronos = request.user.cliente  # Definir cliente_kronos
            nova_tarefa.save()  # Salva a nova tarefa com o cliente_kronos
            messages.success(request, 'Tarefa cadastrada com sucesso!')
            return redirect('lista_tarefas')  # Substitua pelo nome da URL de destino desejada
    else:
        form = TarefaForm()  # Cria uma instância do formulário para GET requests

    tarefas = Tarefa.objects.filter(cliente_kronos=request.user.cliente)  # Filtra as tarefas pelo cliente do usuário
    return render(request, 'task/lista_tarefas.html', {'tarefas': tarefas, 'form': form})


def detalhe_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)  # Pegue a tarefa específica ou retorne 404
    return render(request, 'task/detalhe_tarefa.html', {'tarefa': tarefa})
