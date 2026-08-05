import django.forms as forms  # type: ignore
from .models import AipData


class AipDataForm(forms.ModelForm):
    class Meta:
        model = AipData
        fields = [
            'server', 'inst_comp_name', 'primary_ip', 'inst_comp_status',
            'aip_status', 'vpdc_profile', 'customer_site_id', 'customer_site_name',
            'rank', 'physical_site_id', 'support_region', 'sales_product_line',
            'service_package',
        ]
        widgets = {
            'server': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Server"}),
            'inst_comp_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Inst Comp Name"}),
            'primary_ip': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Primary IP"}),
            'inst_comp_status': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Inst Comp Status"}),
            'aip_status': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter AIP Status"}),
            'vpdc_profile': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter VPDC Profile"}),
            'customer_site_id': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Customer Site Id"}),
            'customer_site_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Customer Site Name"}),
            'rank': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Rank"}),
            'physical_site_id': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Physical Site Id"}),
            'support_region': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Support Region"}),
            'sales_product_line': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Sales Product Line"}),
            'service_package': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Service Package"}),
        }
        labels = {
            'server': 'Server',
            'inst_comp_name': 'Inst Comp Name',
            'primary_ip': 'Primary IP',
            'inst_comp_status': 'Inst Comp Status',
            'aip_status': 'AIP Status',
            'vpdc_profile': 'VPDC Profile',
            'customer_site_id': 'Customer Site Id',
            'customer_site_name': 'Customer Site Name',
            'rank': 'Rank',
            'physical_site_id': 'Physical Site Id',
            'support_region': 'Support Region',
            'sales_product_line': 'Sales Product Line',
            'service_package': 'Service Package',
        }

    def clean(self):
        cleaned_data = super().clean()
        char_fields = [
            'server', 'inst_comp_name', 'primary_ip', 'inst_comp_status',
            'aip_status', 'vpdc_profile', 'customer_site_id', 'customer_site_name',
            'rank', 'physical_site_id', 'support_region', 'sales_product_line',
            'service_package',
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