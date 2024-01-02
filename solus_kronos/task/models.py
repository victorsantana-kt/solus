from django.db import models
from django.contrib.auth.models import User
from clientes_kronos.models import Cliente  # Substitua pelo caminho correto do modelo Cliente
from produtos.models import Produto         # Substitua pelo caminho correto do modelo Produto
from django.conf import settings  # Importe as configurações
class StatusTarefa(models.TextChoices):
    AGUARDANDO = 'AG', 'Aguardando'
    CONCLUIDO = 'CO', 'Concluído'
    EM_ATRASO = 'EA', 'Em Atraso'

class AreaTarefa(models.TextChoices):
    FINANCEIRO = 'FI', 'Financeiro'
    PESSOAL = 'PE', 'Pessoal'
    PROCESSOS = 'PR', 'Processos'
    COMERCIAL = 'CO', 'Comercial'
    # ... outros conforme necessário

class Tarefa(models.Model):
    status = models.CharField(
        max_length=2,
        choices=StatusTarefa.choices,
        default=StatusTarefa.AGUARDANDO
    )
    descricao = models.TextField()
    responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use AUTH_USER_MODEL para referenciar o modelo de usuário personalizado
        on_delete=models.CASCADE,
        related_name='tarefas'
    )
    prazo = models.DateField()
    area = models.CharField(
        max_length=2,
        choices=AreaTarefa.choices
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='tarefas'
    )
    cliente_kronos  = models.ForeignKey('clientes_kronos.Cliente', on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Verificando se é uma nova instância
            self.cliente_kronos = self.responsavel.cliente  # Atribui o cliente do responsável à tarefa
            # Define o produto como "task" se não estiver definido
        if not self.pk and not self.produto:  # Verificando se é uma nova instância e produto não está definido
            produto_task, created = Produto.objects.get_or_create(nome="task")  # Busca ou cria o produto "task"
            self.produto = produto_task
        super(Tarefa, self).save(*args, **kwargs)  # Chama o método save original
    
    def __str__(self):
        return self.descricao
