from django import forms
from .models import Livros

class LivrosForm(forms.ModelForm):

	#titulo_livro = forms.CharField(max_length=200)
	#autor_livro = forms.CharField(max_length=200)
	#editora_livro = forms.CharField(max_length=200)
	#categoria_livro =  forms.CharField(max_length=200)
	
	class Meta:
		model = Livros
		fields = '__all__'