from django.shortcuts import render, redirect  # type: ignore
from django.contrib import messages  # type: ignore
from django.contrib.auth.hashers import check_password, make_password  # type: ignore
from django.utils.decorators import method_decorator  # type: ignore
from django.http import HttpRequest, HttpResponse  # type: ignore
from django.http import JsonResponse  # type: ignore
from django.core import signing  # type: ignore
from django.db import models  # type: ignore

from Main.auth_utils import access_required
from Main.csv_utils import write_csv_row
from .models import Employee
from .forms import EmployeeForm, EmployeeLoginForm, EmployeeForgotForm, EmployeeResetForm, EmployeeChangePasswordForm

RESET_TOKEN_SALT = 'employee-forgot-password-reset'
RESET_TOKEN_TTL = 3000  # 50 minutes

def generate_reset_token(employee: Employee) -> str:
    return signing.dumps({'emp': employee.id}, salt=RESET_TOKEN_SALT)

def verify_reset_token(token: str):  # returns Employee or None
    try:
        data = signing.loads(token, max_age=RESET_TOKEN_TTL, salt=RESET_TOKEN_SALT)
        emp_id = data.get('emp')
        return Employee.objects.filter(id=emp_id).first()
    except signing.SignatureExpired:
        return None
    except signing.BadSignature:
        return None

# Create your views here.
@access_required
def view(request):
    #order by active,Firstname & lastname
    employees = Employee.objects.order_by('-is_active', 'first_name', 'last_name')
    return render(request, 'Employee/view.html', {'employees': employees})

@access_required
def add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Employee:view')
    else:
        form = EmployeeForm()
    return render(request, 'Employee/add.html', {'form': form})

@access_required
def edit(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        #print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('Employee:view')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'Employee/edit.html', {'form': form, 'id': id})

@access_required
def delete(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('Employee:view')
    return render(request, 'Employee/delete.html', {'employee': employee})

@access_required
def export(request):
    import csv
    from django.http import HttpResponse # type: ignore
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'
    writer = csv.writer(response)
    writer.writerow(['Sno', 'First Name', 'Last Name', 'CUID', 'Role', 'Location','Employee Code','Designation','Manager Name','Phone','Email','Is Active','Hired Date'])
    employees = Employee.objects.all()
    for i, v in enumerate(employees, start=1):
        write_csv_row(writer, [i, v.first_name, v.last_name, v.cuid, v.role.name, v.location.name, v.employee_code, v.designation, v.manager_name, v.phone, v.email, v.is_active, v.hired_date])
    return response


def login(request):
    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['identifier']
            password = form.cleaned_data['password']
            employee = Employee.objects.filter(
                models.Q(email__iexact=identifier) |
                models.Q(cuid__iexact=identifier) |
                models.Q(employee_code__iexact=identifier)
            ).first()
            if employee:
                #print(employee)
                stored = employee.password.strip()
                authenticated = False
                if stored:
                    try:
                        if check_password(password, stored):
                            authenticated = True
                        elif stored == password:
                            employee.password = make_password(password)
                            employee.save(update_fields=['password'])
                            authenticated = True
                    except Exception:
                        print("Exception in hashed password check, trying legacy")
                        if stored == password:
                            employee.password = make_password(password)
                            employee.save(update_fields=['password'])
                            authenticated = True                                
                if authenticated:
                    request.session['id'] = employee.id
                    request.session['first_name'] = employee.first_name
                    request.session['last_name'] = employee.last_name
                    request.session['cuid'] = employee.cuid
                    request.session['employee_code'] = employee.employee_code
                    request.session['email'] = employee.email
                    request.session['rolename'] = employee.role.name
                    request.session['roleid'] = employee.role.id
                    request.session['designation'] = employee.designation
                    return redirect('Employee:view')
            messages.error(request, 'Invalid email or password.')
    else:
        form = EmployeeLoginForm()
    form1 = EmployeeForgotForm()
    return render(request, 'auth/login.html', {'form': form, 'form1': form1})


def logout(request):
    request.session.flush()
    return redirect('/home')

def forgot_password(request):
    if request.method == 'POST':
        form = EmployeeForgotForm(request.POST)
        if form.is_valid():
            cuid = form.cleaned_data['cuid']
            email = form.cleaned_data['email']
            employee_code = form.cleaned_data['employee_code']
            employee = Employee.objects.filter(cuid__iexact=cuid, email__iexact=email, employee_code__iexact=employee_code).first()
            if not employee:
                messages.error(request, 'No matching employee found.')
            else:
                token = generate_reset_token(employee)
                reset_link = request.build_absolute_uri(f"/reset-password/{token}/")
                # In production send via email. For now, display on page.
                return render(request, 'auth/forgot_password.html', {'form': form, 'reset_link': reset_link, 'token_expires_in': RESET_TOKEN_TTL})
    else:
        form = EmployeeForgotForm()
    return render(request, 'auth/forgot_password.html', {'form': form})


def reset_password(request, token: str):
    employee = verify_reset_token(token)
    #print(employee)
    
    if not employee:
        #print("Expired")
        messages.error(request, 'Invalid or expired reset link.')
        return redirect('forgot_password')
    if request.method == 'POST':
        #print("posted")
        form = EmployeeResetForm(request.POST)
        if form.is_valid():
            pwd = form.cleaned_data['password']
            #print(employee)
            # Hash and save
            employee.password = make_password(pwd)
            employee.save(update_fields=['password'])
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = EmployeeResetForm(initial={'token': token})
    return render(request, 'auth/reset_password.html', {'form': form, 'expires_in': RESET_TOKEN_TTL})

def change_password(request):
    if request.method == 'POST':
        form = EmployeeChangePasswordForm(request.POST)
        if form.is_valid():
            pwd = form.cleaned_data['new_password']
            curr_pwd = form.cleaned_data['current_password']
            emp_id = request.session.get('id')
            employee = Employee.objects.filter(id=emp_id).first()
            if employee and check_password(curr_pwd, employee.password):
                employee.password = make_password(pwd)
                employee.save(update_fields=['password'])
                messages.success(request, 'Password has been changed successfully.')
                return redirect('Employee:view')
            else:
                messages.error(request, 'Invalid current password.')
    else:
        form = EmployeeChangePasswordForm()
    return render(request, 'Employee/change_password.html', {'form': form})