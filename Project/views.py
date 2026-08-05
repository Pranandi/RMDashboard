from django.shortcuts import render, redirect 
from Main.auth_utils import access_required
from Main.csv_utils import write_csv_row
from .forms import ProjectForm
from .models import Project


@access_required
def view(request):
    projects = Project.objects.all()
    return render(request, 'Project/view.html', {'projects': projects})

@access_required
def add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Project:view')
    else:
        form = ProjectForm()
    return render(request, 'Project/add.html', {'form': form})

@access_required
def edit(request, id):
    project = Project.objects.get(id=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('Project:view')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'Project/edit.html', {'form': form, 'id': id})

@access_required
def delete(request, id):
    project = Project.objects.get(id=id)
    if request.method == 'POST':
        project.delete()
        return redirect('Project:view')
    return render(request, 'Project/delete.html', {'project': project})

@access_required
def export(request):
    import csv
    from django.http import HttpResponse 
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="projects.csv"'
    writer = csv.writer(response)
    writer.writerow(['Sno', 'Name', 'Code', 'Description'])
    projects = Project.objects.all()
    for i, v in enumerate(projects, start=1):
        write_csv_row(writer, [i, v.name, v.code, v.description])
    return response