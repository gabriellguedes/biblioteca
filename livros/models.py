from django.db import models

# Create your models here.
class Livros(models.Model):
	id_livro = models.AutoField(primary_key=True)
	titulo_livro = models.CharField(max_length=200)
	autor_livro = models.CharField(max_length=200)
	editora_livro = models.CharField(max_length=200)
	categoria_livro =  models.CharField(max_length=200)
	
	def __unicode__(self):
		return '%s - %s' %(self.id_livro, self.titulo_livro)	