from django.contrib import admin
from .models import *

## base

@admin.register(NivelDificuldade)
class NivelDificuldadeAdmin(admin.ModelAdmin):
    list_display = ('nivel_dificuldade',)
    search_fields = ('nivel_dificuldade',)

@admin.register(NivelEnsino)
class NivelEnsinoAdmin(admin.ModelAdmin):
    list_display = ('nivel_ensino',)
    search_fields = ('nivel_ensino',)

## Área, subárea e matéria

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Subarea)
class SubareaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'area')
    search_fields = ('nome',)
    list_filter = ('area',)
    
@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'subarea', 'nivel_dificuldade')
    search_fields = ('nome',)
    list_filter = ('subarea__area','subarea', 'nivel_dificuldade')

## Conteudo, módulo, curso, questão e teste

class AuthorAdminMixin:
    """Mixin para restringir visualização, edição e exclusão aos próprios itens."""

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)

    def has_change_permission(self, request, obj=None):
        """Permite edição apenas se o usuário for o autor."""
        if obj is None:
            return True
        return request.user.is_superuser or obj.autor == request.user

    def has_delete_permission(self, request, obj=None):
        """Permite exclusão apenas se o usuário for o autor."""
        if obj is None:
            return True
        return request.user.is_superuser or obj.autor == request.user

@admin.register(Conteudo)
class ConteudoAdmin(AuthorAdminMixin, admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_postagem', 'materia', 'materia__nivel_ensino')
    search_fields = ('titulo',)
    list_filter = ('autor', 'materia', 'data_postagem', 'materia__nivel_ensino')
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.autor = request.user
        super().save_model(request, obj, form, change)
    
@admin.register(Modulo)
class ModuloAdmin(AuthorAdminMixin, admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_postagem', 'subarea')
    search_fields = ('titulo',)
    list_filter = ('autor', 'subarea', 'data_postagem')
    
    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.autor = request.user
        super().save_model(request, obj, form, change)

@admin.register(Curso)
class CursoAdmin(AuthorAdminMixin, admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_postagem', 'area')
    search_fields = ('titulo',)
    list_filter = ('autor', 'area', 'data_postagem')
    
    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.autor = request.user
        super().save_model(request, obj, form, change)

@admin.register(Teste)
class TesteAdmin(AuthorAdminMixin, admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_postagem', 'materia')
    search_fields = ('titulo',)
    list_filter = ( 'autor', 'materia', 'data_postagem', 'nivel_dificuldade', 'materia__nivel_ensino')
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.autor = request.user
        super().save_model(request, obj, form, change)

@admin.register(Questao)
class QuestaoAdmin(AuthorAdminMixin, admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_postagem', 'materia')
    search_fields = ('titulo',)
    list_filter = ('autor', 'materia', 'data_postagem', 'nivel_dificuldade', 'materia__nivel_ensino')
    
    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.autor = request.user
        super().save_model(request, obj, form, change)
    
## Comentário

@admin.register(ComentarioConteudo)
class ComentarioConteudoAdmin(AuthorAdminMixin, admin.ModelAdmin):
    list_display = ('autor', 'conteudo__titulo', 'comentario')
    list_filter = ('autor',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.autor = request.user
        super().save_model(request, obj, form, change)


