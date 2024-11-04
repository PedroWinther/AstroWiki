from django import forms
from .models import Conteudo, Modulo, Curso

class ConteudoForm(forms.ModelForm):
    class Meta:
        model = Conteudo
        fields = ['titulo', 'descricao', 'conteudo', 'materia']  

class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['subarea', 'conteudos']  

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'descricao', 'area', 'modulos']  
        

