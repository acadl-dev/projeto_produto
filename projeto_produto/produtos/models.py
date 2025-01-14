from django.core.exceptions import ValidationError
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.preco <= 0:
            raise ValidationError({'preco': 'O preço deve ser maior que zero.'})
        if self.quantidade_estoque < 0:
            raise ValidationError({'quantidade_estoque': 'A quantidade em estoque não pode ser negativa.'})

    def __str__(self):
        return self.nome
