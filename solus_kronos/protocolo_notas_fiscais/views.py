import datetime
from django.shortcuts import render, redirect
from .forms import NotaFiscalForm,NotaFiscalFilterForm
from .models import NotaFiscal
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import NotaFiscalForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import NotaFiscalForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import NotaFiscalForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from produtos.models import Produto, ClienteProduto
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from app477.models import Bd477 


@login_required
def teste_view(request):
    return render(request, 'protocolo_notas_fiscais/teste.html')


@login_required
def editar_nf(request, nf_id):
    nf = get_object_or_404(NotaFiscal, id=nf_id)

    if request.method == 'POST':
        form = NotaFiscalForm(request.POST, instance=nf)
        if form.is_valid():
            nf = form.save(commit=False)
            nf.data_ultima_alteracao = timezone.now()
            nf.save()
            return redirect('listar_nfs')  # Substitua pelo nome da sua view de listagem de NFs
    else:
        form = NotaFiscalForm(instance=nf)

    return render(request, 'protocolo_notas_fiscais/editar_nf.html', {'form': form})
@login_required
def cadastrar_nf(request):
    if request.method == 'POST':
        form = NotaFiscalForm(request.POST, request.FILES)
        if form.is_valid():
            nota_fiscal = form.save(commit=False)
            nota_fiscal.usuario_cadastrou = request.user

            # Verifique se o usuário tem um cliente associado e atribua à NF
            if hasattr(request.user, 'cliente') and request.user.cliente is not None:
                nota_fiscal.cliente_associado = request.user.cliente
            else:
                # Se o usuário não tem cliente associado, retorne um erro ou uma mensagem
                # Este passo é importante para evitar IntegrityError
                return render(request, 'protocolo_notas_fiscais/error.html', {
                    'message': 'Usuário não possui cliente associado.'
                })

            nota_fiscal.save()
            return redirect('listar_nfs')  # Redireciona para a listagem após o cadastro
    else:
        form = NotaFiscalForm()

    return render(request, 'protocolo_notas_fiscais/cadastrar_nf.html', {'form': form})

    
    
@login_required
def listar_nfs(request):
    
    # Verifica se o cliente do usuário tem acesso ao produto "Protocolo de Nfs"
    try:
        produto_protocolo_nfs = Produto.objects.get(nome='Protocolo de Nfs')
        if not ClienteProduto.objects.filter(cliente=request.user.cliente, produto=produto_protocolo_nfs).exists():
            return render(request, 'lobby/acesso_proibido.html')
    except Produto.DoesNotExist:
        return render(request, 'lobby/acesso_proibido.html')
    
    filtro_form = NotaFiscalFilterForm(request.GET or None)
    nf_query = NotaFiscal.objects.all()

    if filtro_form.is_valid():
        if filtro_form.cleaned_data.get("nome_fornecedor"):
            nf_query = nf_query.filter(nome_fornecedor__icontains=filtro_form.cleaned_data["nome_fornecedor"])
        if filtro_form.cleaned_data.get("cnpj_fornecedor"):
            nf_query = nf_query.filter(cnpj_fornecedor__icontains=filtro_form.cleaned_data["cnpj_fornecedor"])
        if filtro_form.cleaned_data.get("numero_nf"):
            nf_query = nf_query.filter(numero_nf=filtro_form.cleaned_data["numero_nf"])
    
    form = NotaFiscalForm()  # Criar uma instância do formulário
    nfs = NotaFiscal.objects.filter(cliente_associado=request.user.cliente)  # Filtra as NFs pelo cliente do usuário logado
    
    # Aqui você carrega as instâncias de NotaFiscal que deseja exibir
    notas_fiscais = NotaFiscal.objects.all()
    
    # Verifica se cada NotaFiscal tem um cod correspondente em Bd477 e atualiza o status
    for nota_fiscal in notas_fiscais:

        if Bd477.objects.filter(cod=nota_fiscal.cod).exists():
            nota_fiscal.status_ssw = 'sim'
            #correspondente = Bd477.objects.filter(cod=nota_fiscal.cod).first()
        else:
            nota_fiscal.status_ssw = 'nao'
        nota_fiscal.save(update_fields=['status_ssw'])
    
    
    return render(request, 'protocolo_notas_fiscais/listar_nfs.html', {'form': form,'filtro_form': filtro_form, 'nfs': nf_query})


@login_required
@require_POST
@csrf_exempt  # Somente se você estiver tendo problemas com CSRF. Idealmente, use o token CSRF.
def atualizar_status_ssw(request):
    if not request.user.groups.filter(name='Contabilidade').exists():
        return JsonResponse({"success": False, "error": "Usuário não tem permissão para esta ação."})
    try:
        nf_id = request.POST.get('nfId')
        status_ssw = request.POST.get('statusSsw')

        nf = NotaFiscal.objects.get(id=nf_id)
        nf.status_ssw = status_ssw
        #nf.data_status_ssw = timezone.now()  # Atualizar a data de status SSW
        nf.usuario_que_mudou_o_status = request.user
        nf.save()

        return JsonResponse({"success": True})
    except NotaFiscal.DoesNotExist:
        return JsonResponse({"success": False, "error": "NF não encontrada"})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})
