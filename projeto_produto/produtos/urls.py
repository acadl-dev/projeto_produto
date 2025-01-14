from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('novo/', views.produto_criar, name='produto_criar'),
    path('<int:id>/editar/', views.produto_editar, name='produto_editar'),
    path('<int:id>/deletar/', views.produto_deletar, name='produto_deletar'),
]
