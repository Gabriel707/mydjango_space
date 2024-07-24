from django.shortcuts import render


def index(request):
    return render(request, 'mariarosashop/index.html')


def imagem(request):
    return render(request, 'mariarosashop/imagem.html')
