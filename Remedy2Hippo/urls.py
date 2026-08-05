from django.urls import path

from .views import callapi, view

app_name = 'Remedy2Hippo'
urlpatterns = [
    path('', view, name='view'),
    path('view/', view, name='view'),
    path('callapi/', callapi, name='callapi'),
]