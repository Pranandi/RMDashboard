import django.forms as forms  # type: ignore
from .models import UploaderVariant


class UploaderVariantForm(forms.ModelForm):
    class Meta:
        model = UploaderVariant
        fields = [
            'template_id', 'last_updated', 'created', 'project',
            'variant_name', 'variant_description', 'default_variant',
            'active', 'impacting', 'mop', 'team_name', 'team_description',
            'variant', 'default_project_variant',
        ]
        widgets = {
            'template_id': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Template ID"}),
            'last_updated': forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
            'created': forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
            'project': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Project"}),
            'variant_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Variant Name"}),
            'variant_description': forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter Variant Description", "rows": 3}),
            'default_variant': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'active': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'impacting': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'mop': forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter MOP", "rows": 3}),
            'team_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Team Name"}),
            'team_description': forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter Team Description", "rows": 3}),
            'variant': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Variant"}),
            'default_project_variant': forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {
            'template_id': 'Template ID',
            'last_updated': 'Last Updated',
            'created': 'Created',
            'project': 'Project',
            'variant_name': 'Variant Name',
            'variant_description': 'Variant Description',
            'default_variant': 'Default Variant',
            'active': 'Active',
            'impacting': 'Impacting',
            'mop': 'MOP',
            'team_name': 'Team Name',
            'team_description': 'Team Description',
            'variant': 'Variant',
            'default_project_variant': 'Default Project Variant',
        }
        error_messages = {
            'template_id': {
                'required': 'Template ID is required.',
                'max_length': 'Template ID cannot exceed 100 characters.',
            },
            'project': {
                'required': 'Project is required.',
                'max_length': 'Project cannot exceed 255 characters.',
            },
            'variant_name': {
                'required': 'Variant Name is required.',
                'max_length': 'Variant Name cannot exceed 255 characters.',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        for field_name in ['template_id', 'project', 'variant_name', 'team_name', 'variant']:
            value = cleaned_data.get(field_name)
            if value:
                cleaned_data[field_name] = value.strip()
        return cleaned_data
