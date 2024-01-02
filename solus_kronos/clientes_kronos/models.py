from django.db import models
import os
from django.utils.deconstruct import deconstructible

@deconstructible
class RenameLogo:
    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        cnpj = instance.cnpj.replace('.', '').replace('/', '').replace('-', '')
        new_filename = f'{cnpj}.{ext}'
        return os.path.join(self.sub_path, new_filename)

class Cliente(models.Model):
    nome_empresa = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=20)
    #logo = models.ImageField(upload_to='static/logos_clientes/', null=True, blank=True)  # Campo novo
    logo = models.ImageField(upload_to=RenameLogo('static/logos_clientes/'), null=True, blank=True)

    # Adicione mais campos conforme necessário
    def save(self, *args, **kwargs):
        try:
            # tenta obter o objeto antigo
            obj = Cliente.objects.get(id=self.id)
        except Cliente.DoesNotExist:
            pass  # se não existir um objeto antigo, não faz nada
        else:
            # se existir um logotipo antigo e ele é diferente do novo
            if obj.logo and self.logo and obj.logo != self.logo:
                obj.logo.delete(save=False)  # deleta o arquivo antigo, sem salvar o objeto

        super(Cliente, self).save(*args, **kwargs)  # continua a salvar normalmente
    def __str__(self):
        return self.nome_empresa
