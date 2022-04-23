from datetime import datetime
from django.shortcuts import redirect, render
from .models import Jobs
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages


def JobsView(request):
    return redirect('encontrar_jobs')

def Encontrar_Jobs(request):
    if request.method == 'GET':
        preco_minimo = request.GET.get('preco_minimo')
        preco_maximo = request.GET.get('preco_maximo')

        prazo_minimo = request.GET.get('prazo_minimo')
        prazo_maximo = request.GET.get('prazo_maximo')

        categoria = request.GET.get('categoria')

        if preco_minimo or preco_maximo or prazo_minimo or prazo_maximo or categoria:
            
            if not preco_minimo:
                preco_minimo = 0

            if not preco_maximo:
                preco_maximo = 999999

            if not prazo_minimo:
                prazo_minimo = datetime(year=1900, month=1, day=1)

            if not prazo_maximo:
                prazo_maximo = datetime(year=3000, month=1, day=1)
        
            if not categoria:
                jobs = Jobs.objects.filter(preco__gte=preco_minimo)\
                .filter(preco__lte=preco_maximo)\
                .filter(prazo_entrega__gte=prazo_minimo)\
                .filter(prazo_entrega__lte=prazo_maximo)\
                .filter(reservado=False)
            else:
                jobs = Jobs.objects.filter(preco__gte=preco_minimo)\
                    .filter(preco__lte=preco_maximo)\
                    .filter(prazo_entrega__gte=prazo_minimo)\
                    .filter(prazo_entrega__lte=prazo_maximo)\
                    .filter(categoria__in=[categoria, ])\
                    .filter(reservado=False)
        
        else:
            jobs = Jobs.objects.filter(reservado=False)

        return render(request, 'encontrar_jobs.html', {'jobs': jobs})


def Aceitar_job(request, id):
    job = Jobs.objects.get(id=id)
    job.profissional = request.user
    job.reservado = True
    job.save()
    return redirect('encontrar_jobs')


def Perfil(request):
    if request.method == 'GET':
        jobs = Jobs.objects.filter(profissional=request.user)
        return render(request, 'perfil.html', {'jobs': jobs})
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')

        if request.user.username != username:
            user = User.objects.filter(username=username).exclude(id=request.user.id)

            if user.exists():
                messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse Username')
                return redirect('perfil')

        if request.user.email != email:
            user = User.objects.filter(email=email).exclude(id=request.user.id)

            if user.exists():
                messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse E-mail')    
                return redirect('perfil')

        if request.user.username != username or request.user.email != email or request.user.first_name != primeiro_nome or request.user.last_name != ultimo_nome:  
            request.user.username = username
            request.user.email = email
            request.user.first_name = primeiro_nome
            request.user.last_name = ultimo_nome
            request.user.save()
            messages.add_message(request, constants.SUCCESS, 'Dados alterado com sucesso')
            return redirect('perfil')
        else:
            messages.add_message(request, constants.INFO, 'Nenhum dado para ser alterado')
            return redirect('perfil')

        
def Enviar_projeto(request):
    if request.method == 'POST':
        arquivo = request.POST.get('file')
        id = request.POST.get('id')

        job = Jobs.objects.get(id=id)
        job.arquivo_final = arquivo
        job.status = 'AA'
        job.save()
        return redirect('perfil')