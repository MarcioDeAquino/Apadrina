from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from .forms import *
from .models import Project


def home(request):
    return render(request, 'base.html')
# Create your views here.


class criar(FormView):
    template_name = 'createProject.html'
    form_class = ProjectForm
    success_url = 'cadastro'

    def form_valid(self, form):

        user = self.request.user
        project = Project()
        project.description = form.cleaned_data['description']
        project.local = form.cleaned_data['local']
        project.name = form.cleaned_data['name']
        project.author = user

        project.save()
        return super(criar, self).form_valid(form)


def teste(request, id):
    print(id)
    project = Project()
    print(project.local)
    return HttpResponse(project)


