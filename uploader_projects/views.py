from django.shortcuts import render, redirect, get_object_or_404  # type: ignore

from Main.auth_utils import access_required
from .forms import UploaderProjectForm
from .models import UploaderProject


@access_required
def view(request):
    items = UploaderProject.objects.all()
    return render(request, 'uploader_projects/view.html', {'items': items})


@access_required
def add(request):
    if request.method == 'POST':
        form = UploaderProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('uploader_projects:view')
    else:
        form = UploaderProjectForm()
    return render(request, 'uploader_projects/add.html', {'form': form})


@access_required
def edit(request, id):
    item = get_object_or_404(UploaderProject, id=id)
    if request.method == 'POST':
        form = UploaderProjectForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('uploader_projects:view')
    else:
        form = UploaderProjectForm(instance=item)
    return render(request, 'uploader_projects/edit.html', {'form': form, 'id': id})


@access_required
def delete(request, id):
    item = get_object_or_404(UploaderProject, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('uploader_projects:view')
    return render(request, 'uploader_projects/delete.html', {'item': item})
