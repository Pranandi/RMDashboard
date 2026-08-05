import django.forms as forms  # type: ignore
from .models import CrqProperties


class CrqPropertiesForm(forms.ModelForm):
    class Meta:
        model = CrqProperties
        fields = [
            'is_impacting',
            'change_type',
            'manager_group',
            'class1',
            'impact',
            'urgency',
            'risk_level',
            'estimated_outage_duration',
            'operational_categorization_1',
            'operational_categorization_2',
            'service_impact_assessment_work_info',
        ]
        widgets = {
            'is_impacting': forms.Select(attrs={"class": "form-control", "placeholder": "Is Impacting"}, choices=[(True, 'True'), (False, 'False')]),
            'change_type': forms.Select(attrs={"class": "form-control", "placeholder": "Enter Change Type"}),
            'manager_group': forms.Select(attrs={"class": "form-control", "placeholder": "Enter Manager Group"}),
            'class1': forms.Select(attrs={"class": "form-control", "placeholder": "Enter Class"}),
            'impact': forms.Select(attrs={"class": "form-control", "placeholder": "Enter Impact"}),
            'urgency': forms.Select(attrs={"class": "form-control", "placeholder": "Enter Urgency"}),
            'risk_level': forms.Select(attrs={"class": "form-control", "placeholder": "Enter Risk Level"}),
            'estimated_outage_duration': forms.Select(attrs={"class": "form-control", "placeholder": "Enter Estimated Outage Duration"}),
            'operational_categorization_1': forms.Select(attrs={"class": "form-control", "placeholder": "Enter Operational Categorization 1"}),
            'operational_categorization_2': forms.Select(attrs={"class": "form-control", "placeholder": "Enter Operational Categorization 2"}),
            'service_impact_assessment_work_info': forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter Service Impact Assessment Work Info", "rows": 4}),
        }
        labels = {
            'is_impacting': 'Is Impacting',
            'change_type': 'Change Type',
            'manager_group': 'Manager Group',
            'class1': 'Class',
            'impact': 'Impact',
            'urgency': 'Urgency',
            'risk_level': 'Risk Level',
            'estimated_outage_duration': 'Estimated Outage Duration',
            'operational_categorization_1': 'Operational Categorization 1',
            'operational_categorization_2': 'Operational Categorization 2',
            'service_impact_assessment_work_info': 'Service Impact Assessment Work Info',
        }
        error_messages = {
            'change_type': {
                'required': 'Change Type is required.',
                'max_length': 'Change Type cannot exceed 100 characters.',
            },
            'manager_group': {
                'required': 'Manager Group is required.',
                'max_length': 'Manager Group cannot exceed 100 characters.',
            },
            'class1': {
                'required': 'Class is required.',
                'max_length': 'Class cannot exceed 100 characters.',
            },
            'impact': {
                'required': 'Impact is required.',
                'max_length': 'Impact cannot exceed 100 characters.',
            },
            'urgency': {
                'required': 'Urgency is required.',
                'max_length': 'Urgency cannot exceed 100 characters.',
            },
            'risk_level': {
                'required': 'Risk Level is required.',
                'max_length': 'Risk Level cannot exceed 100 characters.',
            },
            'estimated_outage_duration': {
                'required': 'Estimated Outage Duration is required.',
                'max_length': 'Estimated Outage Duration cannot exceed 100 characters.',
            },
            'operational_categorization_1': {
                'required': 'Operational Categorization 1 is required.',
                'max_length': 'Operational Categorization 1 cannot exceed 100 characters.',
            },
            'operational_categorization_2': {
                'required': 'Operational Categorization 2 is required.',
                'max_length': 'Operational Categorization 2 cannot exceed 100 characters.',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        char_fields = [
            'change_type', 'manager_group', 'class1', 'impact', 'urgency',
            'risk_level', 'estimated_outage_duration',
            'operational_categorization_1', 'operational_categorization_2',
        ]
        for field_name in char_fields:
            value = cleaned_data.get(field_name)
            if value:
                cleaned_data[field_name] = value.strip()
        return cleaned_data
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance