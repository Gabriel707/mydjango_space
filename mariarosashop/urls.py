from django.urls import path
from mariarosashop.views import index, imagem

urlpatterns = [
    path('', index),
    path('imagem/', imagem)
]
