from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def buscar(request):
    query = request.GET.get('q')  # Obter o termo de pesquisa do parâmetro 'q'
    resultados_conteudos = Conteudo.objects.filter(titulo__icontains=query)
    resultados_modulos = Modulo.objects.filter(titulo__icontains=query)
    resultados_cursos = Curso.objects.filter(titulo__icontains=query)

    context = {
        'query': query,
        'resultados_conteudos': resultados_conteudos,
        'resultados_modulos': resultados_modulos,
        'resultados_cursos': resultados_cursos,
    }
    return render(request, 'buscar.html', context)

@login_required
def home(request):
    
    continue_conteudos = Conteudo.objects.all()[:4]
    suggestion_conteudos = Conteudo.objects.all()[4:8]
    
    context = {
        'is_autor_or_admin': request.user.is_authenticated and request.user.tipo_usuario in ['autor', 'administrador'],
        'continue_conteudos': continue_conteudos,
        'suggestion_conteudos': suggestion_conteudos,
    }
    
    return render(request, 'index.html', context)

## comentários

def excluir_comentario(comentario):
    """ Helper function to delete a comment """
    if comentario.comentario_pai:
        # Remove a resposta
        comentario.delete()
    else:
        # Remove o comentário principal e suas respostas
        comentario.respostas.all().delete()
        comentario.delete()
        
@login_required
def excluir_comentario_conteudo(request, comentario_id):
    comentario = get_object_or_404(ComentarioConteudo, id=comentario_id)
    if request.user == comentario.autor or request.user.is_superuser:
        excluir_comentario(comentario)
    return redirect(request.META.get('HTTP_REFERER', 'conteudo_detail'))

# --- Views de Detalhe para Conteudo, Modulo, Curso, Teste, Questao ---

@login_required
def conteudo_detail(request, conteudo_id):
    conteudo = get_object_or_404(Conteudo, id=conteudo_id)
    comentarios = ComentarioConteudo.objects.filter(conteudo=conteudo, comentario_pai=None).order_by('-id')

    if request.method == 'POST':
        comentario_texto = request.POST.get('comentario')
        comentario_pai_id = request.POST.get('comentario_pai')
        if comentario_texto:
            comentario_pai = ComentarioConteudo.objects.filter(id=comentario_pai_id).first() if comentario_pai_id else None
            ComentarioConteudo.objects.create(
                conteudo=conteudo,
                autor=request.user,
                comentario=comentario_texto,
                comentario_pai=comentario_pai
            )
            return redirect('conteudo_detail', conteudo_id=conteudo_id)

    return render(request, 'conteudo_detail.html', {'conteudo': conteudo, 'comentarios': comentarios})

@login_required
def modulo_detail(request, modulo_id):
    modulo = get_object_or_404(Modulo, id=modulo_id)
    comentarios = ComentarioModulo.objects.filter(modulo=modulo, comentario_pai=None).order_by('-id')

    if request.method == 'POST':
        comentario_texto = request.POST.get('comentario')
        comentario_pai_id = request.POST.get('comentario_pai')
        if comentario_texto:
            comentario_pai = ComentarioModulo.objects.filter(id=comentario_pai_id).first() if comentario_pai_id else None
            ComentarioModulo.objects.create(
                modulo=modulo,
                autor=request.user,
                comentario=comentario_texto,
                comentario_pai=comentario_pai
            )
            return redirect('modulo_detail', modulo_id=modulo_id)

    return render(request, 'modulo_detail.html', {'modulo': modulo, 'comentarios': comentarios})

@login_required
def curso_detail(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    comentarios = ComentarioCurso.objects.filter(curso=curso, comentario_pai=None).order_by('-id')

    if request.method == 'POST':
        comentario_texto = request.POST.get('comentario')
        comentario_pai_id = request.POST.get('comentario_pai')
        if comentario_texto:
            comentario_pai = ComentarioCurso.objects.filter(id=comentario_pai_id).first() if comentario_pai_id else None
            ComentarioCurso.objects.create(
                curso=curso,
                autor=request.user,
                comentario=comentario_texto,
                comentario_pai=comentario_pai
            )
            return redirect('curso_detail', curso_id=curso_id)

    return render(request, 'curso_detail.html', {'curso': curso, 'comentarios': comentarios})

@login_required
def teste_detail(request, teste_id):
    teste = get_object_or_404(Teste, id=teste_id)
    comentarios = ComentarioTeste.objects.filter(teste=teste, comentario_pai=None).order_by('-id')

    if request.method == 'POST':
        comentario_texto = request.POST.get('comentario')
        comentario_pai_id = request.POST.get('comentario_pai')
        if comentario_texto:
            comentario_pai = ComentarioTeste.objects.filter(id=comentario_pai_id).first() if comentario_pai_id else None
            ComentarioTeste.objects.create(
                teste=teste,
                autor=request.user,
                comentario=comentario_texto,
                comentario_pai=comentario_pai
            )
            return redirect('teste_detail', teste_id=teste_id)

    return render(request, 'teste_detail.html', {'teste': teste, 'comentarios': comentarios})

@login_required
def questao_detail(request, questao_id):
    questao = get_object_or_404(Questao, id=questao_id)
    comentarios = ComentarioQuestao.objects.filter(questao=questao, comentario_pai=None).order_by('-id')

    if request.method == 'POST':
        comentario_texto = request.POST.get('comentario')
        comentario_pai_id = request.POST.get('comentario_pai')
        if comentario_texto:
            comentario_pai = ComentarioQuestao.objects.filter(id=comentario_pai_id).first() if comentario_pai_id else None
            ComentarioQuestao.objects.create(
                questao=questao,
                autor=request.user,
                comentario=comentario_texto,
                comentario_pai=comentario_pai
            )
            return redirect('questao_detail', questao_id=questao_id)

    return render(request, 'questao_detail.html', {'questao': questao, 'comentarios': comentarios})


# --- Views de Listagem para Conteudo, Modulo, Curso, Teste, Questao ---

def listar_conteudos(request):
    conteudos = Conteudo.objects.all()
    return render(request, 'listar_conteudos.html', {'conteudos': conteudos})

def listar_modulos(request):
    modulos = Modulo.objects.all()
    return render(request, 'listar_modulos.html', {'modulos': modulos})

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'listar_cursos.html', {'cursos': cursos})

def listar_testes(request):
    testes = Teste.objects.all()
    return render(request, 'listar_testes.html', {'testes': testes})

def listar_questoes(request):
    questoes = Questao.objects.all()
    return render(request, 'listar_questoes.html', {'questoes': questoes})

