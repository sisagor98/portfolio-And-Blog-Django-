from django.shortcuts import render
from .models import Project


def index(request):
    project = Project.objects.all()
    context = {
        'projects': project,
    }
    return render(request, 'project/index.html', context)


def detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'projects': project,
    }
    return render(request, 'project/detail.html', context)

