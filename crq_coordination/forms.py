import django.forms as forms  # type: ignore
from .models import CrqCoordination


class CrqCoordinationForm(forms.ModelForm):
    class Meta:
        model = CrqCoordination
        fields = ['coordination', 'coordinator_company', 'coordinator_organization', 'workgroup', 'change_coordinator', 'task_name', 'task_summary']
        widgets = {
            'coordination': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Coordination"}),
            'coordinator_company': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Coordinator Company"}),
            'coordinator_organization': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Coordinator Organization"}),
            'workgroup': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Workgroup"}),
            'change_coordinator': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Change Coordinator"}),
            'task_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Task Name"}),
            'task_summary': forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter Task Summary", "rows": 4}),
        }
        labels = {
            'coordination': 'Coordination',
            'coordinator_company': 'Coordinator Company',
            'coordinator_organization': 'Coordinator Organization',
            'workgroup': 'Workgroup',
            'change_coordinator': 'Change Coordinator',
            'task_name': 'Task Name',
            'task_summary': 'Task Summary',
        }
        error_messages = {
            'coordination': {
                'required': 'Coordination is required.',
                'max_length': 'Coordination cannot exceed 100 characters.',
            },
            'coordinator_company': {
                'required': 'Coordinator Company is required.',
                'max_length': 'Coordinator Company cannot exceed 100 characters.',
            },
            'coordinator_organization': {
                'required': 'Coordinator Organization is required.',
                'max_length': 'Coordinator Organization cannot exceed 100 characters.',
            },
            'workgroup': {
                'required': 'Workgroup is required.',
                'max_length': 'Workgroup cannot exceed 100 characters.',
            },
            'change_coordinator': {
                'required': 'Change Coordinator is required.',
                'max_length': 'Change Coordinator cannot exceed 100 characters.',
            },
            'task_name': {
                'max_length': 'Task Name cannot exceed 100 characters.',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        for field_name in ['coordination', 'coordinator_company', 'coordinator_organization', 'workgroup', 'change_coordinator', 'task_name']:
            value = cleaned_data.get(field_name)
            if value:
                cleaned_data[field_name] = value.strip()
        return cleaned_data
    
    def save(self, commit = True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance