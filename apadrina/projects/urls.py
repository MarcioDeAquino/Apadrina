from django.urls import path

from . import  views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='main'),
    path('criarEvento', views.criar.as_view(), name='criar'),
    path('colab/<int:id>', views.teste, name='colaborar'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
