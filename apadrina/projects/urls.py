from django.urls import path

from . import  views

urlpatterns = [
    path('', views.home, name='main'),
    path('criarEvento', views.criar.as_view(), name='criar'),
    path('colab/', views.colab, name='open'),
    path('colab/<int:id>', views.teste, name='colaborar'),
]