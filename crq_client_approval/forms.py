import django.forms as forms

from clients.models import Clients  # type: ignore
from uploader_projects.models import UploaderProject  # type: ignore
from .models import CrqClientApproval


class CrqClientApprovalForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        queryset=Clients.objects.filter(is_active=True).order_by('client_name'),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label='Select Client'
    )
    template = forms.ModelChoiceField(
        queryset=UploaderProject.objects.order_by('project'),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label='Select Template'
    )

    class Meta:
        model = CrqClientApproval
        fields = ['client', 'template', 'approval_note']
        widgets = {
            'approval_note': forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter Approval Note", "rows": 4}),
        }
        labels = {
            'client': 'Client',
            'template': 'Template',
            'approval_note': 'Approval Note',
        }
        error_messages = {
            'client': {
                'required': 'Client is required.',
            },
            'template': {
                'required': 'Template is required.',
                'max_length': 'Template cannot exceed 255 characters.',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['template'].label_from_instance = lambda obj: obj.project

    def clean(self):
        return super().clean()
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
