from django.db import models

# Create your models here.

class Venda(models.Model):
    mes = models.CharField(max_length=20)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.mes}: {self.quantidade}"