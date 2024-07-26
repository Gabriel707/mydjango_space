from django.shortcuts import render
from mariarosashop.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'mariarosashop/index.html', {"cards": fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'mariarosashop/imagem.html', {"fotografia": fotografia})
