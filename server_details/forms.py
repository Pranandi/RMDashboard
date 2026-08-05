import django.forms as forms

from django.db.models import Min

from .models import ServerDetails
from clients.models import Clients

class ServerDetailsForm(forms.ModelForm):    
    class Meta:   
        client_choices = list(set([client.vantive_name for client in Clients.objects.filter(is_active=True).order_by('vantive_name')]))     
        model = ServerDetails
        fields = ['batch','client', 'server', 'operating_system', 'application', 'environment', 'server_type', 'notes', 'include']
        widgets = {
            'batch': forms.Select(attrs={"class": "form-control",}),
            'client': forms.Select(attrs={"class": "form-control"},choices=[('', '---------')] + [(client, client) for client in client_choices]),
            'operating_system': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Operating System"}),
            'server': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Server"}),
            'application': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Application"}),
            'environment': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Environment"}),
            'server_type': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Server Type"}),
            'notes': forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter Notes", "rows": 4}),
            'include': forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            'batch': 'Batch',
            'client': 'Client',
            'server': 'Server',
            'operating_system': 'Operating System',
            'application': 'Application',
            'environment': 'Environment',
            'server_type': 'Server Type',
            'notes': 'Notes',
            'include': 'Include',
        }

    def clean(self):
        return super().clean()

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
