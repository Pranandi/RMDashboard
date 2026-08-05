from django.shortcuts import render, redirect, get_object_or_404  # type: ignore

from Main.auth_utils import access_required
from .forms import TimezoneTableForm
from .models import TimezoneTable


@access_required
def view(request):
    items = TimezoneTable.objects.all()
    return render(request, 'timezone_table/view.html', {'items': items})


@access_required
def add(request):
    if request.method == 'POST':
        form = TimezoneTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timezone_table:view')
    else:
        form = TimezoneTableForm()
    return render(request, 'timezone_table/add.html', {'form': form})


@access_required
def edit(request, id):
    item = get_object_or_404(TimezoneTable, id=id)
    if request.method == 'POST':
        form = TimezoneTableForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('timezone_table:view')
    else:
        form = TimezoneTableForm(instance=item)
    return render(request, 'timezone_table/edit.html', {'form': form, 'id': id})


@access_required
def delete(request, id):
    item = get_object_or_404(TimezoneTable, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('timezone_table:view')
    return render(request, 'timezone_table/delete.html', {'item': item})
