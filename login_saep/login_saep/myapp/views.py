from django.shortcuts import render, redirect
from myapp.models import Usuario


# Criação das views
def listar_usuarios(request):
    value = Usuario.objects.all()
    nome = request.GET.get('nome')
    if nome: value = value.filter(nome__icontains=nome)  # Filtra pelo nome caso seja fornecido
    return render(request, 'myapp/globals/listar.html', {"lista_usuarios": value})


def criar_usuarios(request):
    nome = None
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        if nome and idade:
            Usuario.objects.create(nome=nome, idade=idade)

    return render(request, 'myapp/globals/cadastrar.html', {"ultimo_nome": nome})


def deletar_usuarios(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect(listar_usuarios)


def atualizar_usuarios(request, id):
    usuario = Usuario.objects.get(id=id)
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        if nome and idade:
            usuario.nome = nome
            usuario.idade = idade
            usuario.save()
            
        return redirect(listar_usuarios)

    return render(request, 'myapp/globals/atualizar.html', {"item": usuario})