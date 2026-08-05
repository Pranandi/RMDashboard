from django.shortcuts import render, redirect # type: ignore

from Main.auth_utils import access_required
from Main.csv_utils import write_csv_row
from .forms import VersionForm
from .models import Version

# Create your views here.
@access_required
def view(request):
    versions = Version.objects.all()
    return render(request, 'Version/view.html', {'versions': versions})

@access_required
def add(request):
    if request.method == 'POST':
        form = VersionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Version:view')
    else:
        form = VersionForm()
    return render(request, 'Version/add.html', {'form': form})

@access_required
def edit(request, id):
    version = Version.objects.get(id=id)
    if request.method == 'POST':
        form = VersionForm(request.POST, instance=version)
        if form.is_valid():
            form.save()
            return redirect('Version:view')
    else:
        form = VersionForm(instance=version)
    return render(request, 'Version/edit.html', {'form': form, 'id': id})

@access_required
def delete(request, id):
    version = Version.objects.get(id=id)
    if request.method == 'POST':
        version.delete()
        return redirect('Version:view')
    return render(request, 'Version/delete.html', {'version': version})

@access_required
def export(request):
    import csv
    from django.http import HttpResponse # type: ignore
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="versions.csv"'
    writer = csv.writer(response)
    writer.writerow(['Sno', 'Project', 'Operation System', 'Version', 'Policy Name', 'Manual File Name', 'Manual File Location', 'Confluence Page Link'])
    versions = Version.objects.all()
    for i, v in enumerate(versions, start=1):
        write_csv_row(writer, [i, v.project, v.operation_system, v.version, v.policy_name, v.manual_file_name, v.manual_file_location, v.confluence_page_link])
    return response