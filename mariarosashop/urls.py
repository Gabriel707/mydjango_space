from django.urls import path
from mariarosashop.views import index

urlpatterns = [
    path('', index),
]