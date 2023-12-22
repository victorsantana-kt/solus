
from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente

def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)  # Incluir request.FILES
        if form.is_valid():
            form.save()
            return redirect('lobby')  # Suponho que 'lobby' seja o nome da sua URL de redirecionamento
    else:
        form = ClienteForm()

    clientes = Cliente.objects.all()  # Busca todos os clientes cadastrados
    return render(request, 'clientes_kronos/criar_cliente.html', {'form': form, 'clientes': clientes})
