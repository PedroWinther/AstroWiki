from django.db import models
from accounts.models import Usuario, NivelEnsino

## corrijir a view de registrar usuário
## dar a opção de atualizae usuário para usuário verificado (talvez adicionar os atributos de usuarioverificado em usuario e deixar eles
## como none inicialmente, e atualizar depois) (talvez mexendo nas views)
 
## base 

class NivelDificuldade(models.Model):
    nivel_dificuldade = models.CharField(max_length=50)
    ## simples, médio, difícil
    def __str__(self):
        return self.nivel_dificuldade

  
## Área, subárea e matéria
## Área -> física, subária -> Mecânica, matéria -> gravitação

class Area(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Subarea(models.Model):
    nome = models.CharField(max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.nome} - {self.area.nome}"
    
class Materia(models.Model):
    nome = models.CharField(max_length=50, default=None)
    subarea = models.ForeignKey(Subarea, on_delete=models.CASCADE, default=None)
    nivel_ensino = models.ForeignKey(NivelEnsino, on_delete=models.CASCADE, default=None)
    nivel_dificuldade = models.ForeignKey(NivelDificuldade, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.nome} - {self.subarea.nome} - {self.subarea.area.nome}"
    

## Conteudo, módulo, curso, questão e teste
## Conteudo -> matéria, módulo -> subárea, curso -> área
## Questão -> matéria, teste -> matéria

## classe mãe 
class Postagem(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None, editable=False)
    data_postagem = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=50, default=None)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.titulo
    
## postagem que precisa de uma descrição
class Material(Postagem):
    descricao = models.CharField(max_length=300, default=None)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.titulo

class Conteudo(Material):
    conteudo = models.TextField()  
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Modulo(Material):
    conteudos = models.ManyToManyField(Conteudo)
    subarea = models.ForeignKey(Subarea, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Curso(Material):
    modulos = models.ManyToManyField(Modulo)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Teste(Material):
    nivel_dificuldade = models.ForeignKey(NivelDificuldade, on_delete=models.CASCADE, default=None)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Questao(Postagem):
    enunciado = models.TextField()  
    alternativas = models.TextField()  
    resposta = models.CharField(max_length=500)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nivel_dificuldade = models.ForeignKey(NivelDificuldade, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    

## Comentário

class Comentario(models.Model):
    comentario = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, editable=False)
    data_comentario = models.DateTimeField(auto_now_add=True)
    comentario_pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='respostas')

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.autor.apelido} - {self.comentario[:20]}..."

class ComentarioConteudo(Comentario):
    conteudo = models.ForeignKey('Conteudo', on_delete=models.CASCADE)

class ComentarioModulo(Comentario):
    modulo = models.ForeignKey('Modulo', on_delete=models.CASCADE)

class ComentarioCurso(Comentario):
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)

class ComentarioTeste(Comentario):
    teste = models.ForeignKey('Teste', on_delete=models.CASCADE)

class ComentarioQuestao(Comentario):
    questao = models.ForeignKey('Questao', on_delete=models.CASCADE)
    