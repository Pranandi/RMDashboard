"""
URL configuration for Main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from Employee.views import login, logout, forgot_password, reset_password
from FrontEnd.views import home, about, employee, project, project_version, escalation, customer, location, role, contact_us, Error404View, get_change_chart_data,monthly_metrics

urlpatterns = [
    path('',home, name='home'),
    path('home/',home, name='home'),
    path('about/', about, name='about'),
    path('organisation/', employee, name='employee'),
    path('projects/', project, name='project'),
    path('projects/<str:i>/', project_version, name='project_version'),
    path('escalation/', escalation, name='escalation'),
    path('customers/', customer, name='customer'),
    path('geo/', location, name='location'),
    path('roles/', role, name='role'),
    path('contact/', contact_us, name='contact_us'),
    path('login/', login, name='login'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('reset-password/<str:token>/', reset_password, name='reset_password'),
    path('logout/', logout, name='logout'),
    path('change-chart-data/', get_change_chart_data, name='get_change_chart_data'),
    path('monthly-metrics/', monthly_metrics, name='monthly_metrics'),
    path('admin/', admin.site.urls),
    path('employee/', include('Employee.urls')),
    path('role/', include('Role.urls')),
    path('location/',include('Location.urls')),
    path('customer/',include('Customer.urls')),
    path('project/',include('Project.urls')),
    path('version/',include('Version.urls')),
    path('coordination-and-execution-escalation/',include('Coordination_and_Execution_Escalation.urls')),
    path('contact-us/', include('ContactUs.urls')),
    path('access-control-role/', include('AccessControl_Role.urls')),
    path('access-control-employee/', include('AccessControl_Employee.urls')),
    path('Changedetails/', include('Changedetails.urls')),
    path('Remedy2Hippo/', include('Remedy2Hippo.urls')),
    path('task-information/', include('task_information.urls')),
    path('clients/', include('clients.urls')),
    path('crq-client-approval/', include('crq_client_approval.urls')),
    path('crq-coordination/', include('crq_coordination.urls')),
    path('crq-additional-tasks/', include('crq_additional_tasks.urls')),
    path('crq-properties/', include('crq_properties.urls')),
    path('dc-region/', include('dc_region.urls')),
    path('uploader-projects/', include('uploader_projects.urls')),
    path('uploader-variants/', include('uploader_variants.urls')),
    path('timezone-table/', include('timezone_table.urls')),
    path('aip-data/', include('aip_data.urls')),
    path('server-details/', include('server_details.urls')),
]

# Custom error handlers
handler404 = 'FrontEnd.views.Error404View'

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])