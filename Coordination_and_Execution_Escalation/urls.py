from django.urls import path
from .views import *

app_name = 'Coordination_and_Execution_Escalation'
urlpatterns = [
    path('', view, name='view'),
    path('add/', add, name='add'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
    path('export/', export, name='export'),
]