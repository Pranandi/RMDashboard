from django.urls import path
from .views import view, edit

app_name = 'changedetails'

urlpatterns = [
    path('', view, name='view'),
    path('view/', view, name='view'),
    path('edit/<int:id>/', edit, name='edit'),
]