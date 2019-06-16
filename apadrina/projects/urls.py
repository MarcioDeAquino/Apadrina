from django.urls import path

from . import  views

from .views import projects

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='main'),
    path('', projects.as_view(), name='projects_list'),
    path('meu_projeto', views.criar.as_view(), name='criar'),
    path('colab/<int:id>', views.teste, name='colaborar'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
