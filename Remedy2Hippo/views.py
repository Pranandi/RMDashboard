from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from django.utils.dateparse import parse_datetime
import os,requests
from django.conf import settings

from Changedetails.models import ChangeDetails


def _to_aware_datetime(value):
    if not value:
        return None
    if isinstance(value, str):
        value = parse_datetime(value)
    if value is None:
        return None
    if timezone.is_naive(value):
        return timezone.make_aware(value)
    return value

# Create your views here.
def view(request):
    #apply filter if change_status is null or not 'CLOSED'
    change_details = ChangeDetails.objects.filter(change_status__isnull=True) | ChangeDetails.objects.exclude(change_status='CLOSED')
    change_details = change_details.order_by('change_number')
    return render(request, 'Remedy2Hippo/view.html', {'change_details': change_details})

def callapi(request):
    if request.method == 'POST':
        change_id = request.POST.get('change_id')
        token = settings.HIPPO_TOKEN
        cert_path = 'hippo.it.savvis.net.crt'  # Path to the certificate file
        url = settings.HIPPO_URL
        url = f"{url}/api/remedy/change/{change_id}"
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }
        arguments = {  }
        try:
            api_response = requests.get(url, headers=headers, params=arguments, verify=cert_path)
            if api_response.status_code != 200:
                error_message = api_response.json().get('message', 'Unknown error occurred')
                return JsonResponse({"error": error_message}, status=api_response.status_code)
            item = api_response.json()
            if ChangeDetails.objects.filter(change_number=item.get('changeId')).exists():
                change_detail = ChangeDetails.objects.get(change_number=item.get('changeId'))
                change_detail.startdate = _to_aware_datetime(item.get('schedule', {}).get('scheduledDates', {}).get('startDate'))
                change_detail.enddate = _to_aware_datetime(item.get('schedule', {}).get('scheduledDates', {}).get('endDate'))
                change_detail.remedy_status = item.get('statusInformation', {}).get('displayReasonName')
                change_detail.remedy_reason = item.get('statusInformation', {}).get('reason')
                change_detail.change_status = item.get('statusInformation', {}).get('current')
                change_detail.company_name = item.get('location', {}).get('company')
                change_detail.save() 
                message = "Change(" + item.get('changeId') + ") updated successfully."
            else:
                message = "Change(" + item.get('changeId') + ") does not exist."
    
            return JsonResponse({"message": message})
        except requests.exceptions.RequestException as e:
            error_message = f"An error occurred: {e}"
            return JsonResponse({"error": error_message}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=405)