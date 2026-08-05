import django.forms as forms  # type: ignore
from .models import TimezoneTable


class TimezoneTableForm(forms.ModelForm):
    class Meta:
        model = TimezoneTable
        fields = [
            'time_zone', 'remedy_tz_dst_inactive', 'remedy_tz_dst_active',
            'non_dst_offset_hours', 'dst_offset', 'offset_mins',
            'dst_start_time', 'dst_end_time', 'utc_offset',
            'daylight_savings_start', 'daylight_savings_end',
        ]
        widgets = {
            'time_zone': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Time Zone"}),
            'remedy_tz_dst_inactive': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Remedy TZ DST Inactive"}),
            'remedy_tz_dst_active': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Remedy TZ DST Active"}),
            'non_dst_offset_hours': forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. -5"}),
            'dst_offset': forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. 1"}),
            'offset_mins': forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. 30"}),
            'dst_start_time': forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. 02:00"}),
            'dst_end_time': forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. 02:00"}),
            'utc_offset': forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. UTC-5"}),
            'daylight_savings_start': forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Mar 2nd Sunday"}),
            'daylight_savings_end': forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Nov 1st Sunday"}),
        }
        labels = {
            'time_zone': 'Time Zone',
            'remedy_tz_dst_inactive': 'Remedy TZ DST Inactive',
            'remedy_tz_dst_active': 'Remedy TZ DST Active',
            'non_dst_offset_hours': 'Non DST Offset Hours',
            'dst_offset': 'DST Offset',
            'offset_mins': 'Offset Mins',
            'dst_start_time': 'DST Start Time',
            'dst_end_time': 'DST End Time',
            'utc_offset': 'UTC Offset',
            'daylight_savings_start': 'Daylight Savings Start',
            'daylight_savings_end': 'Daylight Savings End',
        }
        error_messages = {
            'time_zone': {
                'required': 'Time Zone is required.',
                'max_length': 'Time Zone cannot exceed 100 characters.',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        char_fields = [
            'time_zone', 'remedy_tz_dst_inactive', 'remedy_tz_dst_active',
            'non_dst_offset_hours', 'dst_offset', 'offset_mins',
            'dst_start_time', 'dst_end_time', 'utc_offset',
            'daylight_savings_start', 'daylight_savings_end',
        ]
        for field_name in char_fields:
            value = cleaned_data.get(field_name)
            if value:
                cleaned_data[field_name] = value.strip()
        return cleaned_data
    
    def save(self, commit = True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
