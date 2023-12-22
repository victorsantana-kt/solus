from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DashboardForm
from django.shortcuts import render
from .models import Dashboard


@login_required
def criar_dashboard(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        if form.is_valid():
            dashboard = form.save(commit=False)  # Salva o formulário, mas ainda não o commita no banco de dados
            dashboard.usuario_cadastrou = request.user  # Define o usuário logado como o usuário que cadastrou
            dashboard.save()  # Agora sim, salva no banco de dados
            return redirect('criar_dashboard')  # Substitua pelo destino desejado
    else:
        form = DashboardForm()

    return render(request, 'dashboards/criar_dashboard.html', {'form': form})




def listar_dashboards(request):
    #dashboards = Dashboard.objects.all()
    dashboards = Dashboard.objects.filter(cliente=request.user.cliente)
    return render(request, 'dashboards/listar_dashboards.html', {'dashboards': dashboards})
