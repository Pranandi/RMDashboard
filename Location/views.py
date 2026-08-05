from django.shortcuts import render, redirect # type: ignore

from Main.auth_utils import access_required
from Main.csv_utils import write_csv_row
from .forms import LocationForm
from .models import Location

# Create your views here.
@access_required
def view(request):
    locations = Location.objects.all()
    return render(request, 'Location/view.html', {'locations': locations})

@access_required
def add(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Location:view')
    else:
        form = LocationForm()
    return render(request, 'Location/add.html', {'form': form})

@access_required
def edit(request, id):
    location = Location.objects.get(id=id)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('Location:view')
    else:
        form = LocationForm(instance=location)
    return render(request, 'Location/edit.html', {'form': form, 'id': id})

@access_required
def delete(request, id):
    location = Location.objects.get(id=id)
    if request.method == 'POST':
        location.delete()
        return redirect('Location:view')
    return render(request, 'Location/delete.html', {'location': location})

@access_required
def export(request):
    import csv
    from django.http import HttpResponse # type: ignore
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="locations.csv"'
    writer = csv.writer(response)
    writer.writerow(['Sno', 'Role', 'Name', 'Address', 'Working Hours', 'Working Days', 'Timezone'])
    locations = Location.objects.all()
    for i, v in enumerate(locations, start=1):
        write_csv_row(writer, [i, v.role, v.name, v.address, v.working_hours, v.working_days, v.timezone])
    return response