from django.shortcuts import render, redirect,get_object_or_404 # type: ignore

from Main.auth_utils import access_required
from Main.csv_utils import write_csv_row
from .forms import ClientsForm
from .models import Clients

# Create your views here.
@access_required
def view(request):
    clients = Clients.objects.filter(is_active=True)
    return render(request, 'clients/view.html', {'clients': clients})

@access_required
def add(request):
    if request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients:view')
    else:
        form = ClientsForm()
    return render(request, 'clients/add.html', {'form': form})

@access_required
def edit(request, id):
    client = get_object_or_404(Clients, id=id)
    if request.method == 'POST':
        form = ClientsForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients:view')
    else:
        form = ClientsForm(instance=client)
    return render(request, 'clients/edit.html', {'form': form, 'id': id})


@access_required
def delete(request, id):
    client = Clients.objects.get(id=id)
    if request.method == 'POST':
        client.delete()
        return redirect('clients:view')
    return render(request, 'clients/delete.html', {'client': client})

@access_required
def export(request):
    import csv
    from django.http import HttpResponse # type: ignore
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="clients.csv"'
    writer = csv.writer(response)
    writer.writerow(['Sno', 'Client Name', 'Vantive Name', 'Site ID', 'Advanced/Essential', 'Start Week', 'Start Day', 'Specific Date', 'Frequency', 'Add Month', 'Notes', 'Ask for Approval in Email', 'Email Greeting', 'Email To', 'Email CC', 'Email BCC'])
    clients = Clients.objects.filter(is_active=True)
    for i, v in enumerate(clients, start=1):
        write_csv_row(writer, [i, v.client_name, v.vantive_name, v.site_id, v.advanced_essential, v.start_week, v.start_day, v.specific_date, v.frequency, v.add_month, v.notes, v.ask_for_approval_in_email, v.email_greeting, v.email_to, v.email_cc, v.email_bcc])
    return response