from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import constants
from django.contrib import messages


def Cadastro(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'GET':
            return render(request,'cadastro.html')
        elif request.method == 'POST':

            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm-password')

            user = User.objects.filter(username=username)

            if len(username.strip()) == 0 or len(password.strip()) == 0:
                messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
                return redirect('auth:cadastro')

            if user:
                messages.add_message(request, constants.ERROR, 'Usuario já existe')
                return redirect('auth:cadastro')

            if not password == confirm_password:
                print(password, confirm_password)
                messages.add_message(request, constants.ERROR, 'Senhas diferentes')
                return redirect('auth:cadastro')

            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.add_message(request, constants.SUCCESS, 'Conta criada com sucesso!')
                return redirect('auth:logar')
            except:
                messages.add_message(request, constants.ERROR, 'Falha interna do sistema, tente novamente')
                return redirect('auth:cadastro')

def Logar(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'GET':
            return render(request,'logar.html')
        elif request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if not user:
                messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
                return redirect('auth:logar')
            else:
                login(request, user)
                return redirect('/')
                



def Sair(request):
    logout(request)
    return redirect('auth:login')
    
