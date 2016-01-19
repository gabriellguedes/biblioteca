from django.shortcuts import render,redirect, get_object_or_404
from livros.models import Livros
from .forms import LivrosForm


def index(request):
	return render(request, 'index.html')

def adicionar(request):
	if request.method =="POST":
		form = LivrosForm(request.POST)
		if form.is_valid():
			post  = form.save(commit=False)
			post.author = request.user
			post.save()
			print 'Livro adicionado com sucesso !'
			return redirect('livros.views.listar')
	else:	
		form = LivrosForm()
	return render(request, 'adicionar.html',{'form': form})

def detalhes(request, pk):
	post = get_object_or_404(Livros, pk=pk)
	return render(request, 'detalhes.html', {'post': post})

def alterar(request, pk):
	post = get_object_or_404(Livros, pk=pk)
	if request.method =="GET":
		form = LivrosForm(request.GET, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            
            return redirect('livros.views.detalhes', pk=post.pk)
	else:
		form = LivrosForm(instance=post)
	return render(request, 'alterar.html', {'form': form})
	
def excluir(request, pk):
	post = get_object_or_404(Livros, pk=pk).delete()
	redirect ('livros.views.detalhes')
	return render(request, 'excluir.html', {'post': post})

def listar(request):
	livros = Livros.objects.all()
	return render(request, 'listar.html', locals())


