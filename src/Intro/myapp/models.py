from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    #categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')

    def __str__(self):
        return self.nome
    

""" from django.db import models

# Create your models here.
class Categoria(models.Model):
    #Representa a categoria de um produto (1 Categoria -> N Produtos).
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Tag(models.Model):
    ### Marcador livre para agrupar produtos (N Produtos <-> N Tags).
    nome = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    # 1 Categoria -> N Produtos (OneToMany via ForeignKey)
    categoria = models.ForeignKey(
        'Categoria',
        on_delete=models.CASCADE,
        related_name='produtos',
        null=True,
        blank=True,
    )

    # N Produtos <-> N Tags (ManyToMany)
    tags = models.ManyToManyField('Tag', related_name='produtos', blank=True)

    def __str__(self):
        return self.nome


class ProdutoDetalhe(models.Model):
    #Detalhes adicionais de um produto (1 Produto -> 1 ProdutoDetalhe).
    produto = models.OneToOneField(
        Produto,
        on_delete=models.CASCADE,
        related_name='detalhe'
    )
    sku = models.CharField("SKU", max_length=40, unique=True)
    estoque = models.PositiveIntegerField(default=0)
    peso_gramas = models.PositiveIntegerField(null=True, blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Detalhe do Produto"
        verbose_name_plural = "Detalhes do Produto"

    def __str__(self):
        return f"Detalhes de {self.produto.nome}"
 """ 

 
