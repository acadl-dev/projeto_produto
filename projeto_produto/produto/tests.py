from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from .models import Produto


class ProdutoModelTest(TestCase):
    """Testes para o modelo Produto."""

    def test_criar_produto_valido(self):
        """Testa se é possível criar um produto com valores válidos."""
        produto = Produto.objects.create(
            nome="Produto Teste",
            preco=100.00,
            quantidade_estoque=10,
        )
        self.assertEqual(produto.nome, "Produto Teste")
        self.assertEqual(produto.preco, 100.00)
        self.assertEqual(produto.quantidade_estoque, 10)

    def test_preco_negativo(self):
        """Testa se o modelo rejeita preços negativos."""
        produto = Produto(nome="Produto Inválido", preco=-50.00, quantidade_estoque=10)
        with self.assertRaises(ValidationError) as context:
            produto.full_clean()
        self.assertIn('O preço deve ser maior que zero.', context.exception.message_dict['preco'])

    def test_quantidade_negativa(self):
        """Testa se o modelo rejeita quantidade negativa."""
        produto = Produto(nome="Produto Inválido", preco=50.00, quantidade_estoque=-10)
        with self.assertRaises(ValidationError) as context:
            produto.full_clean()
        self.assertIn('A quantidade em estoque não pode ser negativa.', context.exception.message_dict['quantidade_estoque'])


class ProdutoViewTest(TestCase):
    """Testes para as views de Produto."""

    def test_criar_produto_via_view(self):
        """Testa se é possível criar um produto via view."""
        response = self.client.post(reverse('produto_criar'), {
            'nome': 'Produto Criado na View',
            'preco': 200.00,
            'quantidade_estoque': 5,
        })
        self.assertEqual(response.status_code, 302)  # Redireciona após criar
        self.assertTrue(Produto.objects.filter(nome='Produto Criado na View').exists())

    def test_criar_produto_invalido_via_view(self):
        """Testa se a view rejeita produtos com dados inválidos."""
        response = self.client.post(reverse('produto_criar'), {
            'nome': '',  # Nome vazio
            'preco': -10.00,  # Preço negativo
            'quantidade_estoque': -5,  # Quantidade negativa
        })
        self.assertEqual(response.status_code, 200)  # Retorna à página com erros
        self.assertContains(response, "Este campo é obrigatório.")  # Nome vazio
        self.assertContains(response, "O preço deve ser maior que zero.")  # Preço negativo
        self.assertContains(response, "O preço deve ser maior que zero.")  # Quantidade negativa
