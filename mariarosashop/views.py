from django.shortcuts import render
from mariarosashop.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'mariarosashop/index.html', {"cards": fotografias})


def imagem(request):
    return render(request, 'mariarosashop/imagem.html')
