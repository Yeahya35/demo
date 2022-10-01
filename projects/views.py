from operator import methodcaller
from django.shortcuts import render, redirect
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
    form = ProjectForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('projects')
    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def updateProject(request, pk):
    projectObj = Project.objects.get(id=pk)
    form = ProjectForm(instance=projectObj)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=projectObj)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def deleteProject(request, pk):
    projectObj = Project.objects.get(id=pk)
    if request.method == 'POST':
        projectObj.delete()
        return redirect('projects')
    context = {'object': projectObj}
    return render(request, 'projects/delete_template.html', context)
