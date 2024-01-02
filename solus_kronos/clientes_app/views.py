# clientes_app/views.py

from django.shortcuts import render, redirect
from .forms import ClienteAppForm
from .models import ClienteApp

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteAppForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  # Redireciona para a view de lista após o cadastro
    else:
        form = ClienteAppForm()

    return render(request, 'clientes_app/cadastrar_cliente.html', {'form': form})


def lista_clientes(request):
    clientes = ClienteApp.objects.all()  # Pega todos os clientes
    if request.method == 'POST':
        form = ClienteAppForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)  # Não salve ainda
            cliente.responsavel = request.user
            form.save()
            return redirect('lista_clientes')  # Redireciona para a view de lista após o cadastro
    else:
        form = ClienteAppForm()
    return render(request, 'clientes_app/lista_clientes.html', {'clientes': clientes,'form':form})