from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils import timezone
from .models import Usuario

def criar_conta(request):
    if request.method == 'POST':
        apelido = request.POST['apelido']
        email = request.POST['email']
        password = request.POST['password']

        usuario = Usuario.objects.create_user(apelido=apelido, email=email, password=password)
        login(request, usuario)
        return redirect('../../')  

    return render(request, 'registrar.html')

def login_usuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        usuario = authenticate(request, username=email, password=senha)

        if usuario is not None:
            usuario.last_login = timezone.now()
            usuario.save()
            login(request, usuario)
            next_url = request.GET.get('next', 'homepage')
            return redirect(next_url)
        else:
            return render(request, 'login.html', {'erro': 'Email ou senha incorretos'})

    return render(request, 'login.html')
