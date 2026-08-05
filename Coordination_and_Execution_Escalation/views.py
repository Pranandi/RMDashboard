from django.shortcuts import render, redirect # type: ignore

from Main.auth_utils import access_required
from Main.csv_utils import write_csv_row
from .forms import CoordinationAndExecutionEscalationForm
from .models import CoordinationAndExecutionEscalation

# Create your views here.
@access_required
def view(request):
    escalations = CoordinationAndExecutionEscalation.objects.all().prefetch_related('employees')
    return render(request, 'Coordination_and_Execution_Escalation/view.html', {'escalations': escalations})

@access_required
def add(request):
    if request.method == 'POST':
        form = CoordinationAndExecutionEscalationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Coordination_and_Execution_Escalation:view')
    else:
        form = CoordinationAndExecutionEscalationForm()
    return render(request, 'Coordination_and_Execution_Escalation/add.html', {'form': form})

@access_required
def edit(request, id):
    escalation = CoordinationAndExecutionEscalation.objects.get(id=id)
    if request.method == 'POST':
        form = CoordinationAndExecutionEscalationForm(request.POST, instance=escalation)
        if form.is_valid():
            form.save()
            return redirect('Coordination_and_Execution_Escalation:view')
    else:
        form = CoordinationAndExecutionEscalationForm(instance=escalation)
    return render(request, 'Coordination_and_Execution_Escalation/edit.html', {'form': form, 'id': id})

@access_required
def delete(request, id):
    escalation = CoordinationAndExecutionEscalation.objects.get(id=id)
    if request.method == 'POST':
        escalation.delete()
        return redirect('Coordination_and_Execution_Escalation:view')
    return render(request, 'Coordination_and_Execution_Escalation/delete.html', {'escalation': escalation})

@access_required
def export(request):
    import csv
    from django.http import HttpResponse # type: ignore
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="coordination_and_execution_escalations.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Level', 'Description', 'Location', 'Employee', 'Contact Type'])
    escalations = CoordinationAndExecutionEscalation.objects.all()
    for i, v in enumerate(escalations, start=1):
        write_csv_row(writer, [i, v.level, v.description, v.location, v.employee, v.contact_type])
    return response