from django.shortcuts import render, redirect # type: ignore

from Main.auth_utils import access_required
from Main.csv_utils import write_csv_row
from .forms import ContactUsForm
from .models import ContactUs

# Create your views here.
@access_required
def view(request):
    contactus = ContactUs.objects.all()
    return render(request, 'ContactUs/view.html', {'contactus': contactus})

@access_required
def add(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ContactUs:view')
    else:
        form = ContactUsForm()
    return render(request, 'ContactUs/add.html', {'form': form})

@access_required
def edit(request, id):
    contact_us = ContactUs.objects.get(id=id)
    if request.method == 'POST':
        form = ContactUsForm(request.POST, instance=contact_us)
        if form.is_valid():
            form.save()
            return redirect('ContactUs:view')
    else:
        form = ContactUsForm(instance=contact_us)
    return render(request, 'ContactUs/edit.html', {'form': form, 'id': id})

@access_required
def delete(request, id):
    contact_us = ContactUs.objects.get(id=id)
    if request.method == 'POST':
        contact_us.delete()
        return redirect('ContactUs:view')
    return render(request, 'ContactUs/delete.html', {'contact_us': contact_us})

@access_required
def export(request):
    import csv
    from django.http import HttpResponse # type: ignore
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Contactus.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'title','email','phone','alternative_phone'])
    contactus = ContactUs.objects.all()
    for i, v in enumerate(contactus, start=1):
        write_csv_row(writer, [i, v.name, v.title, v.email, v.phone, v.alternative_phone])
    return response