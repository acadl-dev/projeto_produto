from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),   # Exibe a lista de produtos.
    path('novo/', views.produto_criar, name='produto_criar'),  # Cria um novo produto.
    path('<int:id>/editar/', views.produto_editar, name='produto_editar'),  # Edita um produto usando o ID.
    path('<int:id>/deletar/', views.produto_deletar, name='produto_deletar'),  # Deleta um produto usando o ID.
]
