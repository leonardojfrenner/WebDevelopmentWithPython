from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=255, default='desconhecido')
    senha = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome_produto = models.CharField(max_length=255)
    preco_produto = models.DecimalField(max_digits=10, decimal_places=2)
    descricao_produto = models.TextField()

    def __str__(self):
        return self.nome_produto

class Imagem(models.Model):
    imagem = models.ImageField(upload_to="imagem_produto")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return self.produto.nome_produto