import django.forms as forms  # type: ignore
from .models import UploaderProject


class UploaderProjectForm(forms.ModelForm):
    class Meta:
        model = UploaderProject
        fields = ['template_id', 'project_id', 'project_title', 'project', 'change_title']
        widgets = {
            'template_id': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Template ID"}),
            'project_id': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Project ID"}),
            'project_title': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Project Title"}),
            'project': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Project"}),
            'change_title': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Change Title"}),
        }
        labels = {
            'template_id': 'Template ID',
            'project_id': 'Project ID',
            'project_title': 'Project Title',
            'project': 'Project',
            'change_title': 'Change Title',
        }
        error_messages = {
            'template_id': {
                'required': 'Template ID is required.',
                'max_length': 'Template ID cannot exceed 100 characters.',
            },
            'project_id': {
                'required': 'Project ID is required.',
                'max_length': 'Project ID cannot exceed 100 characters.',
            },
            'project_title': {
                'required': 'Project Title is required.',
                'max_length': 'Project Title cannot exceed 255 characters.',
            },
            'project': {
                'required': 'Project is required.',
                'max_length': 'Project cannot exceed 255 characters.',
            },
            'change_title': {
                'required': 'Change Title is required.',
                'max_length': 'Change Title cannot exceed 255 characters.',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        for field_name in ['template_id', 'project_id', 'project_title', 'project', 'change_title']:
            value = cleaned_data.get(field_name)
            if value:
                cleaned_data[field_name] = value.strip()
        return cleaned_data
    
    def save(self, commit = True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
