from functools import wraps
from django.shortcuts import redirect, render  # type: ignore
from django.contrib import messages  # type: ignore
from django.apps import apps
from AccessControl_Role.models import AccessControl_Role
from AccessControl_Employee.models import AccessControl_Employee



def access_required(view_func):
    """Decorator enforcing that the user is logged in.

    Redirects to named route 'login' if not logged in. Adjust name if project root changes.
    """
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not request.session.get('id'):
            messages.warning(request, 'Please login to continue.')
            return redirect('login')
        view = view_func.__name__
        app = get_app_label(view_func)
        if Check_access(request, view,app):
            pass  # User has access
        else:
            messages.error(request, 'You do not have permission to perform that action.')
            # Redirect to a safe default (employee listing if available)
            data = {
                'code' : 403,
                'type' : 'Access Denied',
                'message' : 'You do not have permission to perform that action.'
            }
            return render(request, 'access-denied.html', data)
        return view_func(request, *args, **kwargs)
    return _wrapped

def Check_access(request, view_name, app_name) -> bool:
    role = request.session.get('rolename', '').lower()
    emp = request.session.get('id')
    operation = ['add','edit','delete','export','view']
    for op in operation:
        request.session[f'can_{op}'] = True
    if role == 'manager':
        for op in operation:
            request.session[f'can_{op}'] = True
        return True
    #print(f"Checking access for view: {view_name} in app: {app_name} for the role {role}")
    #return True  # Temporary override for testing purposes
    role_obj = AccessControl_Role.objects.all().filter(role__name__iexact=role, app_name__iexact=app_name).values('id','role_id','app_name','can_view','can_add','can_edit','can_delete','can_export').first()
    #print(role_obj)
    if role_obj:
        for op in operation:
            request.session[f'can_{op}'] = role_obj[f'can_{op}']
    #for op in operation:
    #    print(op +"=="+str(request.session[f'can_{op}']))
    emp_obj = AccessControl_Employee.objects.all().filter(employee_id=emp, app_name__iexact=app_name).values('id','employee_id','app_name','can_view','can_add','can_edit','can_delete','can_export').first()
    if emp_obj:
        for op in operation:
            if not request.session.get(f'can_{op}'):
                request.session[f'can_{op}'] = emp_obj[f'can_{op}']
                
    for op in operation:
        if view_name.lower() == op:
            return request.session[f'can_{op}']

    return False  # Default deny

def get_app_label(view_func):
    module = view_func.__module__
    for cfg in apps.get_app_configs():
        if module.startswith(cfg.name):
            return cfg.label
    return module.split('.')[0]

