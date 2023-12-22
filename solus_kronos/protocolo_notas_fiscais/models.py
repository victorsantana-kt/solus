from django.db import models
from django.conf import settings
import os
from django.utils.deconstruct import deconstructible
from django.apps import apps
@deconstructible
class RenameNFFile:
    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # Utilizando numero_nf e cnpj_fornecedor para o novo nome do arquivo
        numero_nf = instance.numero_nf
        cnpj = instance.cnpj_fornecedor.replace('.', '').replace('/', '').replace('-', '')
        new_filename = f'{numero_nf}_{cnpj}.{ext}'
        return os.path.join(self.sub_path, new_filename)
    
class NotaFiscal(models.Model):
    nome_fornecedor = models.CharField(max_length=100)
    cnpj_fornecedor = models.CharField(max_length=18)
    numero_nf = models.CharField(max_length=20)
    usuario_cadastrou = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cliente_associado = models.ForeignKey('clientes_kronos.Cliente', on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_emissao_nf = models.DateField()
    descricao = models.TextField()
    #arquivo_nf = models.FileField(upload_to='notas_fiscais/')
    arquivo_nf = models.FileField(upload_to=RenameNFFile('notas_fiscais/'))
    STATUS_CHOICES = (
        ('sim', 'Sim'),
        ('nao', 'Não'),
    )
    status_ssw = models.CharField(max_length=3, choices=STATUS_CHOICES, default='nao')
    usuario_que_mudou_o_status = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='nf_status_modificador')
    data_ultima_alteracao = models.DateTimeField(null=True, blank=True)
    data_status_ssw = models.DateTimeField(null=True, blank=True)
    boleto = models.FileField(upload_to='boletos/',null=True,blank=True)
    cod = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.boleto:
            ext = self.boleto.name.split('.')[-1]
            numero_nf = self.numero_nf
            cnpj = self.cnpj_fornecedor.replace('.', '').replace('/', '').replace('-', '')
            new_filename = f'boleto_{numero_nf}_{cnpj}.{ext}'
            self.boleto.name = os.path.join('notas_fiscais/', new_filename)
            if self.numero_nf and self.cnpj_fornecedor:
                self.cod = f'{self.numero_nf}_{self.cnpj_fornecedor.replace(".", "").replace("/", "").replace("-", "")}'
        # Obtém o modelo Bd477 dinamicamente para evitar importação circular
        Bd477 = apps.get_model('app477', 'Bd477')

        # Verifica se existe um registro correspondente no app477_bd477
        if Bd477.objects.filter(cod=self.cod).exists():
            self.status_ssw = 'sim'
        else:
            self.status_ssw = 'nao'

        super(NotaFiscal, self).save(*args, **kwargs)


    def get_arquivo_url(self):
        if self.arquivo_nf:
            return self.arquivo_nf.url
        return None
    
    def get_boleto_url(self):
        if self.boleto:
            return self.boleto.url
        return None