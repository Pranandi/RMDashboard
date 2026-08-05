from django.shortcuts import render, redirect # type: ignore

from Main.auth_utils import access_required
from Main.csv_utils import write_csv_row
from .forms import RoleForm
from .models import Role

# Create your views here.
@access_required
def view(request):
    roles = Role.objects.all()
    return render(request, 'Role/view.html', {'roles': roles})

@access_required
def add(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Role:view')
    else:
        form = RoleForm()
    return render(request, 'Role/add.html', {'form': form})

@access_required
def edit(request, id):
    role = Role.objects.get(id=id)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('Role:view')
    else:
        form = RoleForm(instance=role)
    return render(request, 'Role/edit.html', {'form': form, 'id': id})

@access_required
def delete(request, id):
    role = Role.objects.get(id=id)
    if request.method == 'POST':
        try:
            role.delete()
        except Exception as e:
            from django.contrib import messages  # type: ignore
            messages.error(request, f'Error deleting role: {str(e)}')
        return redirect('Role:view')
    return render(request, 'Role/delete.html', {'role': role})

@access_required
def export(request):
    import csv
    from django.http import HttpResponse # type: ignore
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="roles.csv"'
    writer = csv.writer(response)
    writer.writerow(['Sno', 'Name', 'Description'])
    roles = Role.objects.all()
    for i, v in enumerate(roles, start=1):
        write_csv_row(writer, [i, v.name, v.description])
    return response