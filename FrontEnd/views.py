from django.shortcuts import render
from django.views.defaults import page_not_found
from django.http import JsonResponse
from django.utils import timezone
from Version.models import Version

def home(request):
    return render(request, 'FrontEnd/home.html')

def about(request):
    return render(request, 'FrontEnd/about.html')

def employee(request):
    from Employee.models import Employee
    employees = Employee.objects.filter(is_active=True).order_by('-role','-designation','first_name').all()
    
    res = []
    emp_dict = {}
    for emp in employees:
        emp_dict[emp.id] = {
            'employee': emp,
            'direct_reports': []
        }
    for emp in employees:
        if emp.manager_name_id and emp.manager_name_id in emp_dict:
            emp_dict[emp.manager_name_id]['direct_reports'].append(emp_dict[emp.id])
        else:
            res.append(emp_dict[emp.id])        
    return render(request, 'FrontEnd/employee.html', {'employees': res})

def project(request):
    from Project.models import Project
    project = Project.objects.all().order_by('id')
    return render(request, 'FrontEnd/project.html', {'projects': project})

def project_version(request, i):
    if i in ['55', '76', '108', 'PS']:
        data = Version.objects.filter(project__code=i).order_by('-id').all()
        max_rows=5
        if i == '55':
            temp = {}
            for item in data:
                if item.version not in temp:
                    temp[item.version] = {}
                temp[item.version][item.operation_system] = {
                    'version': item.version,
                    'policy_name': item.policy_name,
                    'manual_file_name': item.manual_file_name,
                    'manual_file_location': item.manual_file_location
                }
                if temp.__len__() >= max_rows:
                    break;
            data = temp
        if i == '76':
            data = data[:max_rows]
        return render(request, "FrontEnd/project_" + str(i) + ".html",{'db':data})
    else:
        return render(request, "FrontEnd/project_not_found.html")

def escalation(request):
    from Coordination_and_Execution_Escalation.models import CoordinationAndExecutionEscalation
    escalations = CoordinationAndExecutionEscalation.objects.all().order_by('level')
    return render(request, 'FrontEnd/coordination_and_execution_escalation.html', {'escalations': escalations})

def customer(request):
    from Customer.models import Customer
    customers = Customer.objects.all().order_by('name')
    return render(request, 'FrontEnd/customer.html', {'customers': customers})

def location(request):
    from Location.models import Location
    locations = Location.objects.all().order_by('id')
    return render(request, 'FrontEnd/location.html', {'locations': locations})

def role(request):
    from Role.models import Role
    roles = Role.objects.exclude(name="Admin").order_by('id').all()
    return render(request, 'FrontEnd/role.html', {'roles': roles})

def contact_us(request):
    from ContactUs.models import ContactUs
    contacts = ContactUs.objects.all().order_by('id')
    return render(request, 'FrontEnd/contact_us.html', {'contacts': contacts})

def Error404View(request, exception=None):
    return render(request, 'FrontEnd/404.html', status=404)

def get_change_chart_data(request):
    from Changedetails.models import ChangeDetails
    from task_information.models import task_information
    try:
        type = request.GET.get('type', None)
        project_type = request.GET.get('project_type', None)
        company_name = request.GET.get('company_name', None)
        date_filter = request.GET.get('date_filter', 'all')
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        qs_change = ChangeDetails.objects
        change_data = {}
        task_data = {}
        data = {}
        if type in ['project', 'company']:
            if type == 'project':
                qs_change = qs_change.values_list('project_type', flat=True)
            if type == 'company':
                qs_change = qs_change.values_list('company_name', flat=True)
            data = {
                'data': sorted(set(qs_change))
            }
        else:
            if date_filter and date_filter != 'all':
                from datetime import datetime, timedelta
                end = timezone.now()
                current_tz = timezone.get_current_timezone()
                if date_filter == 'last_24':
                    start = end - timedelta(hours=24)
                else:
                    end = end.replace(hour=0, minute=0, second=0, microsecond=0)
                    if date_filter == 'last_7':
                        start = end - timedelta(days=7)
                    elif date_filter == 'last_14':
                        start = end - timedelta(days=14)
                    elif date_filter == 'last_30':
                        start = end - timedelta(days=30)
                    elif date_filter == 'curr_month':
                        start = end.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
                        if start == end:
                            start = end.replace(month=end.month-1, day=1, hour=0, minute=0, second=0, microsecond=0)
                    elif date_filter == 'curr_year':
                        start = end.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
                    elif date_filter == 'last_month':
                        start = (end - timedelta(days=31)).replace(day=1, hour=0, minute=0, second=0)
                        end = (start + timedelta(days=31)).replace(day=1, hour=0, minute=0, second=0)
                    elif date_filter == 'custom':
                        start = timezone.make_aware(datetime.strptime(start_date, '%Y-%m-%d'), current_tz)
                        end = timezone.make_aware(datetime.strptime(end_date, '%Y-%m-%d'), current_tz) + timedelta(days=1)
                print("Start Date:", start, "End Date:", end)
                qs_change = qs_change.filter(startdate__gte=start).filter(startdate__lt=end)
                start_date = start
                end_date = end
            data['company_name']=sorted(set(qs_change.values_list('company_name', flat=True)))
            if company_name and company_name != 'All':
                qs_change = qs_change.filter(company_name=company_name)
            data['project_type']=sorted(set(qs_change.values_list('project_type', flat=True)))
            if project_type and project_type != 'All':
                qs_change = qs_change.filter(project_type=project_type)
            
            qs_task = task_information.objects.filter(change_number_id__in=qs_change.values_list('change_id', flat=True))
            
            data['selected_company_name'] = company_name
            data['selected_project_type'] = project_type if len(data['project_type']) > 1 else data['project_type'][0]
            status_counts = {}
            success_count = qs_change.filter(final_status='Success').count()
            if success_count > 0:
                status_counts['Successful'] = success_count
            partial_count = qs_change.filter(final_status='Partial').count()
            if partial_count > 0:
                status_counts['Partial'] = partial_count
            failed_count = qs_change.filter(final_status='Failed').count() + qs_change.filter(final_status='Unknown').count()
            if failed_count > 0:
                status_counts['Failed'] = failed_count
            total_count = qs_change.count()
            metrics = status_counts.copy()
            metrics['Total'] = total_count
            change_data = {
                'metrics': metrics,
                'pie_labels': list(status_counts.keys()),
                'pie_data': list(status_counts.values()),
                'pie_total': total_count
            }
            
            # Task metrics
            status_counts = {}
            success_count = qs_task.filter(manual_status='Success').count()
            if success_count > 0:
                status_counts['Success'] = success_count
            warning_count = qs_task.filter(manual_status='Warning').count()
            if warning_count > 0:
                status_counts['Warning'] = warning_count
            failed_count = qs_task.filter(manual_status='Failed').count() + qs_task.filter(manual_status='Unknown').count()
            if failed_count > 0:
                status_counts['Failed'] = failed_count
            total_count = qs_task.count()
            metrics = status_counts.copy()
            metrics['Total'] = total_count
            task_data = {
                'metrics': metrics,
                'pie_labels': list(status_counts.keys()),
                'pie_data': list(status_counts.values()),
                'pie_total': total_count
            }
            
            if date_filter and date_filter != 'all':
                data['start_date'] = start_date.strftime('%Y-%m-%d %H:%M:%S')
                data['end_date'] = (end_date- timedelta(seconds=1)).strftime('%Y-%m-%d %H:%M:%S') 
            data['change']= change_data
            data['task'] = task_data
        data['status'] = 'success'
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
def monthly_metrics(request):
    from Changedetails.models import ChangeDetails
    from task_information.models import task_information
    from datetime import timedelta
    current_time = timezone.now()
    #get current month
    start_date = current_time.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    if start_date.day == current_time.day:
        start_date = (start_date - timedelta(days=1)).replace(day=1)
    end_date = (start_date + timedelta(days=31)).replace(day=1)
    data = []
    temp_max_range = int(start_date.strftime('%m'))
    max_range = temp_max_range
    if temp_max_range <=1:
        max_range+=12
    max_date = end_date
    if end_date >= current_time:
        end_date = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
        max_date = end_date
    for i in range(max_range):
        print("Monthly-Start Date:", start_date, "End Date:", end_date)
        qs_change = ChangeDetails.objects.filter(startdate__gte=start_date).filter(startdate__lt=end_date)
        qs_task = task_information.objects.filter(change_number_id__in=qs_change.values_list('change_id', flat=True))
        total_changes = qs_change.count()
        total_tasks = qs_task.count()
        success_changes = str(((qs_change.filter(final_status='Success').count()/total_changes)*100 if total_changes > 0 else 0).__round__(2)) + "%("+str(qs_change.filter(final_status='Success').count())+")"
        partial_changes = str(((qs_change.filter(final_status='Partial').count()/total_changes)*100 if total_changes > 0 else 0).__round__(2)) + "%("+str(qs_change.filter(final_status='Partial').count())+")"
        failed_changes = str((((qs_change.filter(final_status='Failed').count() + qs_change.filter(final_status='Unknown').count())/total_changes)*100 if total_changes > 0 else 0).__round__(2)) + "%("+str(qs_change.filter(final_status='Failed').count() + qs_change.filter(final_status='Unknown').count())+")"
        success_tasks = str(((qs_task.filter(manual_status='Success').count()/total_tasks)*100 if total_tasks > 0 else 0).__round__(2)) + "%("+str(qs_task.filter(manual_status='Success').count())+")"
        warning_tasks = str(((qs_task.filter(manual_status='Warning').count()/total_tasks)*100 if total_tasks > 0 else 0).__round__(2)) + "%("+str(qs_task.filter(manual_status='Warning').count())+")"
        failed_tasks = str((((qs_task.filter(manual_status='Failed').count() + qs_task.filter(manual_status='Unknown').count())/total_tasks)*100 if total_tasks > 0 else 0).__round__(2)) + "%("+str(qs_task.filter(manual_status='Failed').count() + qs_task.filter(manual_status='Unknown').count())+")"
        from_date = start_date.strftime('%d-%b-%Y %H:%M:%S')
        to_date = (end_date - timedelta(seconds=1)).strftime('%d-%b-%Y %H:%M:%S')
        j=i+1
        '''
        if end_date >= max_date:
            success_changes+="<b style='color:red'>*</b>"
            partial_changes += "<b style='color:red'>*</b>"
            failed_changes += "<b style='color:red'>*</b>"
            success_tasks += "<b style='color:red'>*</b>"
            warning_tasks += "<b style='color:red'>*</b>"
            failed_tasks += "<b style='color:red'>*</b>"
            from_date += "<b style='color:red'>*</b>"
            to_date += "<b style='color:red'>*</b>"
            j = str(j) + "<b style='color:red'>*</b>"
            '''
        data.append([j, from_date, to_date, total_changes,success_changes, partial_changes, failed_changes, total_tasks,success_tasks, warning_tasks, failed_tasks])
        start_date = (start_date - timedelta(days=1)).replace(day=1)
        end_date = (start_date + timedelta(days=31)).replace(day=1)
    
    if temp_max_range <=1:
        start_date = (current_time -timedelta(days=365)).replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        end_date = current_time.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    else:
        start_date = current_time.replace(month=1,day=1, hour=0, minute=0, second=0, microsecond=0)
        end_date = current_time.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    qs_change = ChangeDetails.objects.filter(startdate__gte=start_date, startdate__lt=end_date)
    qs_task = task_information.objects.filter(change_number_id__in=qs_change.values_list('change_id', flat=True))
    total_changes = qs_change.count()
    total_tasks = qs_task.count()
    success_changes = str(((qs_change.filter(final_status='Success').count()/total_changes)*100 if total_changes > 0 else 0).__round__(2)) + "%("+str(qs_change.filter(final_status='Success').count())+")"
    partial_changes = str(((qs_change.filter(final_status='Partial').count()/total_changes)*100 if total_changes > 0 else 0).__round__(2)) + "%("+str(qs_change.filter(final_status='Partial').count())+")"
    failed_changes = str((((qs_change.filter(final_status='Failed').count() + qs_change.filter(final_status='Unknown').count())/total_changes)*100 if total_changes > 0 else 0).__round__(2)) + "%("+str(qs_change.filter(final_status='Failed').count() + qs_change.filter(final_status='Unknown').count())+")"
    success_tasks = str(((qs_task.filter(manual_status='Success').count()/total_tasks)*100 if total_tasks > 0 else 0).__round__(2)) + "%("+str(qs_task.filter(manual_status='Success').count())+")"
    warning_tasks = str(((qs_task.filter(manual_status='Warning').count()/total_tasks)*100 if total_tasks > 0 else 0).__round__(2)) + "%("+str(qs_task.filter(manual_status='Warning').count())+")"
    failed_tasks = str((((qs_task.filter(manual_status='Failed').count() + qs_task.filter(manual_status='Unknown').count())/total_tasks)*100 if total_tasks > 0 else 0).__round__(2)) + "%("+str(qs_task.filter(manual_status='Failed').count() + qs_task.filter(manual_status='Unknown').count())+")"
    from_date = start_date.strftime('%d-%b-%Y %H:%M:%S')
    to_date = (end_date - timedelta(seconds=1)).strftime('%d-%b-%Y %H:%M:%S')
    data.append(['<b>Total</b>', '<b>'+from_date+'</b>', '<b>'+to_date+'</b>', '<b>'+str(total_changes)+'</b>', '<b>'+success_changes+'</b>', '<b>'+partial_changes+'</b>', '<b>'+failed_changes+'</b>', '<b>'+str(total_tasks)+'</b>', '<b>'+success_tasks+'</b>', '<b>'+warning_tasks+'</b>', '<b>'+failed_tasks+'</b>'])
    return JsonResponse({'status': 'success', 'data': data,'max_date': (max_date - timedelta(seconds=1)).strftime('%d-%b-%Y %H:%M:%S')})