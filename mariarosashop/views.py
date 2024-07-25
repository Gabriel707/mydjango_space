from django.shortcuts import render


def index(request):

    dados = {
        1: {"nome": "Nebulosa de Carina",
            "legenda": "webtelescope.org / NASA /James Webb"},
        2: {"nome": "Galaxia NGC 1079",
            "legenda": "nada.org / NASA / Hubble"}
    }

    return render(request, 'mariarosashop/index.html', {"cards": dados})


def imagem(request):
    return render(request, 'mariarosashop/imagem.html')
