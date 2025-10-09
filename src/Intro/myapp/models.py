from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    #categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')

    def __str__(self):
        return self.nome
 
#class Categoria(models.Model):
#           nome = models.CharField(max_length=100)
#
#            def __str__(self):
#                return self.nome

""" class Pedido(models.Model):
    produtos = models.ManyToManyField(Produto, through='PedidoProduto', related_name='pedidos')
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido #{self.id}'

class PedidoProduto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome} (Pedido #{self.pedido.id})' """