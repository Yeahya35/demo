from django.shortcuts import render
from .models import Project
from .forms import ProjectForm


def projects(request):
    projectList = Project.objects.all()
    context = {'projects': projectList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': projectObj})


def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, "projects/project_form.html", context)
