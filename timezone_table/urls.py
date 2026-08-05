from django.urls import path
from .views import *

app_name = 'timezone_table'
urlpatterns = [
    path('', view, name='view'),
    path('add/', add, name='add'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
]
