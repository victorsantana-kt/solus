from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class ClienteProduto(models.Model):
    cliente = models.ForeignKey('clientes_kronos.Cliente', on_delete=models.CASCADE)
    produto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cliente.nome_empresa} - {self.produto.nome}"
    
    
