from django.urls import path
from .views import *

app_name = 'crq_client_approval'
urlpatterns = [
    path('', view, name='view'),
    path('add/', add, name='add'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
]
