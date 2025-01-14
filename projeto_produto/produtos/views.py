from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm
from django.contrib import messages

def lista_produtos(request):
    
    ordenacao = request.GET.get('ordenacao', 'nome')  # Ordenar por 'nome' por padrão
    if ordenacao not in ['nome', '-nome', 'preco', '-preco']:
        ordenacao = 'nome'

    produtos = Produto.objects.all().order_by(ordenacao)

    # URLs para ordenação
    ordenacao_nome = 'nome' if ordenacao != 'nome' else '-nome'
    ordenacao_preco = 'preco' if ordenacao != 'preco' else '-preco'

    return render(
        request,
        'produtos/lista_produtos.html',
        {
            'produtos': produtos,
            'ordenacao_nome': ordenacao_nome,
            'ordenacao_preco': ordenacao_preco,
            'ordenacao': ordenacao,
        },
    )

def produto_criar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            messages.success(request, "Produto salvo com sucesso!")
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/produto_form.html', {'form': form, 'title': 'Novo Produto'})

def produto_editar(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            messages.success(request, f"Produto '{produto}' atualizado com sucesso!")
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/produto_form.html', {'form': form, 'title': 'Editar Produto'})

def produto_deletar(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        messages.success(request, f"Produto '{produto}' excluído com sucesso!")
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'produtos/produto_confirm_delete.html', {'produto': produto})
