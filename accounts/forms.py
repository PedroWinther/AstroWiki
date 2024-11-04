from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        tipo_usuario = cleaned_data.get('tipo_usuario')
        
        # Exigir campos para Autor e Administrador
        if tipo_usuario in ['autor', 'administrador']:
            if not cleaned_data.get('nome_completo'):
                self.add_error('nome_completo', 'Nome completo é obrigatório para autores e administradores.')
            if not cleaned_data.get('cpf'):
                self.add_error('cpf', 'CPF é obrigatório para autores e administradores.')
            if not cleaned_data.get('data_nascimento'):
                self.add_error('data_nascimento', 'Data de nascimento é obrigatória para autores e administradores.')
        return cleaned_data


