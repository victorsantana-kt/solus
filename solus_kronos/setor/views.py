from django.shortcuts import render, redirect
from .models import Setor
from .forms import SetorForm

def cadastrar_setor(request):
    if request.method == 'POST':
        form = SetorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')  # Substitua pela sua URL de redirecionamento
    else:
        form = SetorForm()
    return render(request, 'setor/cadastrar_setor.html', {'form': form})

def listar_setores(request):
    setores = Setor.objects.all()
    return render(request, 'setor/listar_setores.html', {'setores': setores})
