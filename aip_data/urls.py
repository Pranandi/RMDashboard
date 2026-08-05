from django.urls import path
from .views import *

app_name = 'aip_data'
urlpatterns = [
    path('', view, name='view'),
    path('add/', add, name='add'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
    path('export/', export, name='export'),
    path('ajax-table/', ajax_table, name='ajax_table'),
]
