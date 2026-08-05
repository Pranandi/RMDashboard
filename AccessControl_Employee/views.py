from django.shortcuts import render, redirect  # type: ignore
from .models import AccessControl_Employee
from .forms import AccessControlEmployeeEditForm,AccessControlEmployeeForm
from Main.auth_utils import access_required
from Main.csv_utils import write_csv_row

# Create your views here.
@access_required
def view(request):
    access_controls = AccessControl_Employee.objects.all()
    return render(request, 'AccessControl_Employee/view.html', {'access_controls': access_controls})

@access_required
def add(request):
    if request.method == 'POST':
        form = AccessControlEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AccessControl_Employee:view')
    else:
        form = AccessControlEmployeeForm()
    return render(request, 'AccessControl_Employee/add.html', {'form': form})

@access_required
def edit(request, id):
    access_control = AccessControl_Employee.objects.get(id=id)
    if request.method == 'POST':
        form = AccessControlEmployeeEditForm(request.POST, instance=access_control)
        if form.is_valid():
            form.save()
            return redirect('AccessControl_Employee:view')
    else:
        form = AccessControlEmployeeEditForm(instance=access_control)
    return render(request, 'AccessControl_Employee/edit.html', {'form': form, 'id': id})

@access_required
def delete(request, id):
    access_control = AccessControl_Employee.objects.get(id=id)
    if request.method == 'POST':
        access_control.delete()
        return redirect('AccessControl_Employee:view')
    return render(request, 'AccessControl_Employee/delete.html', {'access_control': access_control})

@access_required
def export(request):
    import csv
    from django.http import HttpResponse # type: ignore
    access_controls = AccessControl_Employee.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="access_controls.csv"'
    writer = csv.writer(response)
    writer.writerow(['Employee', 'App Name', 'Can View', 'Can Add', 'Can Edit', 'Can Delete', 'Can Export'])
    for ac in access_controls:
        write_csv_row(writer, [ac.employee.username, ac.app_name, ac.can_view, ac.can_add, ac.can_edit, ac.can_delete, ac.can_export])
    return response