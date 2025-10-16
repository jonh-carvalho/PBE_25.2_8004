from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    #categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')

    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    data_pedido = models.DateTimeField(auto_now_add=True)
    produtos = models.ManyToManyField('Produto', through='ItemPedido', related_name='pedidos')

    def __str__(self):
        return f"Pedido #{self.pk} - {self.data_pedido:%d/%m/%Y %H:%M}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    class Meta:
        unique_together = ('pedido', 'produto')

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} (Pedido #{self.pedido.pk})"
    
