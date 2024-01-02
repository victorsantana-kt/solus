from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm  # Importa o formulário personalizado de criação de usuário
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from produtos.models import Produto, ClienteProduto

from django.contrib.auth.views import LoginView

# Decorador que assegura que apenas usuários autenticados acessem a view
@login_required
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')  # Redireciona para a página de registro (ou outra página conforme necessário)
    else:
        form = CustomUserCreationForm()

    # Busca todos os usuários cadastrados
    usuarios = get_user_model().objects.all()

    return render(request, 'accounts/register.html', {'form': form, 'usuarios': usuarios})

# Classe baseada em view para o login, extendendo a LoginView padrão do Django
class CustomLoginView(LoginView):
    # Define o template para a página de login
    template_name = 'accounts/old_login.html'
    # Se o usuário já estiver autenticado, ele será redirecionado
    redirect_authenticated_user = True

    # Define a URL para redirecionar após um login bem-sucedido
    def get_success_url(self):
        return '/'  # Altere para o caminho desejado após o login

# Decorador que exige que o usuário esteja autenticado para acessar a view
@login_required
def edit_user(request):
    # Verifica se a requisição é do tipo POST
    if request.method == 'POST':
        # Cria um formulário preenchido com os dados do usuário atual e os dados enviados
        form = CustomUserChangeForm(request.POST, instance=request.user)
        # Verifica se o formulário é válido
        if form.is_valid():
            # Salva as alterações do usuário no banco de dados
            form.save()
            # Redireciona para a página inicial ou outra página após a edição
            return redirect('/')  # Redirecione para onde você achar melhor
    else:
        # Se não for um POST, exibe um formulário preenchido com os dados atuais do usuário
        form = CustomUserChangeForm(instance=request.user)
    
    # Renderiza a página de edição do usuário com o formulário
    return render(request, 'accounts/edit_user.html', {'form': form})



@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Importante para manter o usuário logado após mudar a senha
            return redirect('/')  # Redirecione para onde você desejar
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/mudar_senha.html', {'form': form})




def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('/')  # Redirecione para a URL após o login bem-sucedido
        else:
            messages.error(request, "Username or password is incorrect")

    return render(request, 'accounts/login.html')  # Nome do seu template de login


    
@login_required
def admin_redirect(request):
    if request.user.is_staff:
        return redirect('/admin/')
    else:
        return render(request, 'lobby/acesso_proibido.html')
    
    

@login_required
def custom_login_redirect(request):
    user = request.user
    cliente = user.cliente

    # Verifica se o cliente está associado ao produto_id=3
    if ClienteProduto.objects.filter(cliente=cliente, produto_id=10).exists():
        return render(request, 'avaliacoes/formulario_avaliacao.html')
    else:
        return redirect('/')
    
# views.py
