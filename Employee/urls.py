from django.urls import path # type: ignore
from .views import *

app_name = 'Employee'
urlpatterns = [
    path('', view, name='view'),
    path('add/', add, name='add'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
    path('export/', export, name='export'),
    path('change-password/', change_password, name='change_password'),
]