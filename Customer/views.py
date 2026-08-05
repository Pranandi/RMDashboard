from django.shortcuts import render, redirect # type: ignore

from Main.auth_utils import access_required
from Main.csv_utils import write_csv_row
from .forms import CustomerForm
from .models import Customer

# Create your views here.
@access_required
def view(request):
    customers = Customer.objects.all()
    return render(request, 'Customer/view.html', {'customers': customers})

@access_required
def add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Customer:view')
    else:
        form = CustomerForm()
    return render(request, 'Customer/add.html', {'form': form})

@access_required
def edit(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('Customer:view')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'Customer/edit.html', {'form': form, 'id': id})

@access_required
def delete(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        customer.delete()
        return redirect('Customer:view')
    return render(request, 'Customer/delete.html', {'customer': customer})

@access_required
def export(request):
    import csv
    from django.http import HttpResponse # type: ignore
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="customers.csv"'
    writer = csv.writer(response)
    writer.writerow(['Sno', 'Name', 'Contact Person Name', 'Contact Person Email', 'Contact Person Phone', 'Confluence Page Link'])
    customers = Customer.objects.all()
    for i, v in enumerate(customers, start=1):
        write_csv_row(writer, [i, v.name, v.contact_person_name, v.contact_person_email, v.contact_person_phone, v.confluence_page_link])
    return response