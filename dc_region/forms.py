import django.forms as forms  # type: ignore
from .models import DcRegion


class DcRegionForm(forms.ModelForm):
    class Meta:
        model = DcRegion
        fields = ['site_id', 'region', 'sub_region', 'country', 'city', 'scheduler_time_zone']
        widgets = {
            'site_id': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Site ID"}),
            'region': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Region"}),
            'sub_region': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Sub Region"}),
            'country': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Country"}),
            'city': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter City"}),
            'scheduler_time_zone': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Scheduler Time Zone"}),
        }
        labels = {
            'site_id': 'Site ID',
            'region': 'Region',
            'sub_region': 'Sub Region',
            'country': 'Country',
            'city': 'City',
            'scheduler_time_zone': 'Scheduler Time Zone',
        }
        error_messages = {
            'site_id': {
                'required': 'Site ID is required.',
                'max_length': 'Site ID cannot exceed 100 characters.',
            },
            'region': {
                'required': 'Region is required.',
                'max_length': 'Region cannot exceed 100 characters.',
            },
            'sub_region': {
                'required': 'Sub Region is required.',
                'max_length': 'Sub Region cannot exceed 100 characters.',
            },
            'country': {
                'required': 'Country is required.',
                'max_length': 'Country cannot exceed 100 characters.',
            },
            'city': {
                'required': 'City is required.',
                'max_length': 'City cannot exceed 100 characters.',
            },
            'scheduler_time_zone': {
                'required': 'Scheduler Time Zone is required.',
                'max_length': 'Scheduler Time Zone cannot exceed 100 characters.',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        for field_name in ['site_id', 'region', 'sub_region', 'country', 'city', 'scheduler_time_zone']:
            value = cleaned_data.get(field_name)
            if value:
                cleaned_data[field_name] = value.strip()
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
