from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import UsuarioForm

@admin.register(Usuario)
class CustomUsuarioAdmin(UserAdmin):
    form = UsuarioForm
    list_display = ['email', 'apelido', 'tipo_usuario', 'is_superuser']
    search_fields = ['email', 'apelido']
    list_filter = ['tipo_usuario', 'is_superuser']
    ordering = ['email']
    
    fieldsets = (
        (None, {'fields': ('email', 'apelido', 'password', 'tipo_usuario')}),
        ('Personal Info', {'fields': ('nome_completo', 'cpf', 'data_nascimento', 'escolaridade')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')
        }),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'apelido', 'password1', 'password2', 'tipo_usuario', 'nome_completo', 'cpf', 'data_nascimento', 'escolaridade', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )