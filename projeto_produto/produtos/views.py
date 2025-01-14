from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm

def produto_list(request):
    
    ordenacao = request.GET.get('ordenacao', 'nome')  
        
    if ordenacao not in ['nome', '-nome', 'preco', '-preco']:
        ordenacao = 'nome'    
        
    produtos = Produto.objects.all().order_by(ordenacao)

    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos, 'ordenacao': ordenacao})

def produto_criar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/produto_form.html', {'form': form, 'title': 'Novo Produto'})

def produto_criar(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/produto_form.html', {'form': form, 'title': 'Editar Produto'})

def produto_deletar(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'produtos/produto_confirm_delete.html', {'produto': produto})
