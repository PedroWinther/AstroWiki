from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='homepage'), 
     # URLs de detalhe
    path('conteudo/<int:conteudo_id>/', conteudo_detail, name='conteudo_detail'),
    path('modulo/<int:modulo_id>/', modulo_detail, name='modulo_detail'),
    path('curso/<int:curso_id>/', curso_detail, name='curso_detail'),
    path('teste/<int:teste_id>/', teste_detail, name='teste_detail'),
    path('questao/<int:questao_id>/', questao_detail, name='questao_detail'),
    
    # URLs de listagem
    path('conteudos/', listar_conteudos, name='listar_conteudos'),
    path('modulos/', listar_modulos, name='listar_modulos'),
    path('cursos/', listar_cursos, name='listar_cursos'),
    path('testes/', listar_testes, name='listar_testes'),
    path('questoes/', listar_questoes, name='listar_questoes'),
    
    # URLs de comentário
    path('conteudo/<int:comentario_id>/excluir/', excluir_comentario_conteudo, name='excluir_comentario_conteudo'),

    # OUTROS
    path('accounts/', include('accounts.urls')), 
    path('buscar/', buscar, name='buscar'), 
]