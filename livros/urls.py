from django.conf.urls import include, url
from . import views

urlpatterns =[  

    url(r'^$', views.index, name='index'),
    url(r'^listar/', views.listar),
    url(r'^livro/(?P<pk>[0-9]+)/$', views.detalhes),
    url(r'^livro/new/$', views.adicionar, name='adicionar' ),
    url(r'^livro/(?P<pk>[0-9]+)/edit/$', views.alterar, name='alterar'),
    url(r'^livro/(?P<pk>[0-9]+)/delete/$', views.excluir, name='excluir'),
    
]