from django.db import models    
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

## base 
class NivelEnsino(models.Model):
    nivel_ensino = models.CharField(max_length=50)
    ## fundamental, médio, superior
    def __str__(self):
        return self.nivel_ensino

## Gerenciador personalizado de usuário
class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, tipo_usuario='aluno', **extra_fields):
        if not email:
            raise ValueError('O endereço de email é obrigatório')
        email = self.normalize_email(email)
        usuario = self.model(email=email, tipo_usuario=tipo_usuario, **extra_fields)
        usuario.set_password(password)
        
        if tipo_usuario == 'administrador':
            usuario.is_staff = True
            usuario.is_superuser = True
        elif tipo_usuario == 'autor':
            usuario.is_staff = True
            usuario.is_superuser = False
        else:
            usuario.is_staff = False
            usuario.is_superuser = False
        
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('tipo_usuario', 'administrador')
        return self.create_user(email, password, **extra_fields)

## Usuário base do site
class Usuario(AbstractBaseUser, PermissionsMixin):
    TIPO_USUARIO_CHOICES = [
        ('aluno', 'Aluno'),
        ('autor', 'Autor'),
        ('administrador', 'Administrador'),
    ]
    
    apelido = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    escolaridade = models.ForeignKey(NivelEnsino, on_delete=models.CASCADE, null=True, blank=True)
    nome_completo = models.CharField(max_length=100, null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES, default='aluno')
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['apelido']

    def __str__(self):
        return f'{self.email} - {self.apelido}'
    
    def save(self, *args, **kwargs):
        if self.tipo_usuario == 'administrador':
            self.is_staff = True
            self.is_superuser = True
        elif self.tipo_usuario == 'autor':
            self.is_staff = True
            self.is_superuser = False
        else:
            self.is_staff = False
            self.is_superuser = False
        super().save(*args, **kwargs)
