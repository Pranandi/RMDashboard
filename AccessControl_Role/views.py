from django.shortcuts import render, redirect # type: ignore

from Main.auth_utils import access_required
from Main.csv_utils import write_csv_row
from .forms import AccessControlRoleEditForm, AccessControlRoleForm
from .models import AccessControl_Role

# Create your views here.
@access_required
def view(request):
    roles = AccessControl_Role.objects.all()
    return render(request, 'AccessControl_Role/view.html', {'roles': roles})

@access_required
def add(request):
    if request.method == 'POST':
        form = AccessControlRoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AccessControl_Role:view')
    else:
        form = AccessControlRoleForm()
    return render(request, 'AccessControl_Role/add.html', {'form': form})

@access_required
def edit(request, id):
    role = AccessControl_Role.objects.get(id=id)
    if request.method == 'POST':
        form = AccessControlRoleEditForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('AccessControl_Role:view')
    else:
        form = AccessControlRoleEditForm(instance=role)
    return render(request, 'AccessControl_Role/edit.html', {'form': form, 'id': id})

@access_required
def delete(request, id):
    role = AccessControl_Role.objects.get(id=id)
    if request.method == 'POST':
        try:
            role.delete()
        except Exception as e:
            from django.contrib import messages  # type: ignore
            messages.error(request, f'Error deleting role: {str(e)}')
        return redirect('AccessControl_Role:view')
    return render(request, 'AccessControl_Role/delete.html', {'role': role})

@access_required
def export(request):
    import csv
    from django.http import HttpResponse # type: ignore
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="roles.csv"'
    writer = csv.writer(response)
    writer.writerow(['Sno', 'Role Name', 'App Name', 'Can View', 'Can Add', 'Can Edit', 'Can Delete', 'Can Export'])
    roles = AccessControl_Role.objects.all()
    for i, v in enumerate(roles, start=1):
        write_csv_row(writer, [i, v.name, v.app_name, v.can_view, v.can_add, v.can_edit, v.can_delete, v.can_export])
    return response