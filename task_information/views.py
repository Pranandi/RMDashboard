from django.shortcuts import render,redirect
from django.http import JsonResponse
import os,requests
from django.conf import settings

from task_information.models import task_information
from Changedetails.models import ChangeDetails

# Create your views here.
def view(request):
    #filter manual status as Unknown, and group by change_number_id, if there are multiple server_name for the same change_number_id, concatenate them with <br/>
    taskinformation = task_information.objects.exclude(manual_status__in=['Success','Failed','Warning']).all().order_by('-change_number_id', 'server_name')
    data = {}
    for item in taskinformation:
        if item.change_number_id in data:
            data[item.change_number_id]['server_name'] += "<br/>\n" + item.server_name + " (" + str(item.manual_status) + ")"
            data[item.change_number_id]['count'] += 1
        else:
            data[item.change_number_id] = {'server_name': item.server_name + " (" + str(item.manual_status) + ")", 'company_name': item.company_name, 'task_id': item.task_id,'count':1}
            change_detail_info = ChangeDetails.objects.filter(change_id=item.change_number_id).all()
            data[item.change_number_id]['change_number'] = change_detail_info[0].change_number if change_detail_info else ''
    return render(request, 'task_information/view.html', {'task_information': data})

def edit(request, id):
    taskinformation = task_information.objects.filter(change_number_id=id).exclude(manual_status__in=['Success','Failed','Warning']).all().order_by('server_name')
    change_detail_info = ChangeDetails.objects.filter(change_id=id).all()
    if request.method == 'POST':
        new_statuses = request.POST.getlist('manual_status[]')
        for new_status in new_statuses:
            task_id, status = new_status.split('||')
            task_information.objects.filter(task_id=task_id).update(manual_status=status)
        return redirect('task_information:view')
    print(taskinformation)
    return render(request, 'task_information/edit.html', {'id':id, 'task_information': taskinformation, 'change_detail_info': change_detail_info})