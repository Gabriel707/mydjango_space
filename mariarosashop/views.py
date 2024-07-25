from django.shortcuts import render
from mariarosashop.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'mariarosashop/index.html', {"cards": dados})


def imagem(request):
    return render(request, 'mariarosashop/imagem.html')
