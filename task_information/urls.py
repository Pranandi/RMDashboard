from django.urls import path
from .views import view, edit

app_name = 'task_information'

urlpatterns = [
    path('', view, name='view'),
    path('edit/<int:id>/', edit, name='edit'),
]