from django.urls import path
from mariarosashop.views import index, imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem')
]
