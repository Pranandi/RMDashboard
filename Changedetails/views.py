from django.shortcuts import render,redirect
from django.http import JsonResponse
import os,requests
from django.conf import settings

from Changedetails.models import ChangeDetails

# Create your views here.
def view(request):
    Change_Details = ChangeDetails.objects.filter(final_status='Unknown').all()
    return render(request, 'ChangeDetails/view.html', {'Change_Detail': Change_Details})

def edit(request, id):
    Change_Details = ChangeDetails.objects.filter(change_id=id).all()
    if request.method == 'POST':
        new_status = request.POST.get('final_status')
        ChangeDetails.objects.filter(change_id=id).update(final_status=new_status)
        return redirect('changedetails:view')
    return render(request, 'ChangeDetails/edit.html', {'id':id, 'Change_Detail': Change_Details})