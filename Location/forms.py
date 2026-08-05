import re
from datetime import time
from zoneinfo import available_timezones

from django import forms # type: ignore
from django.core.exceptions import ValidationError # type: ignore

from Role.models import Role
from .models import Location

# Precompiled patterns
NAME_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 _\-\.&()]{1,98}$")  # basic, adjustable
WORKING_HOURS_PATTERN = re.compile(r"^(?P<sh>[01]\d|2[0-3]):(?P<sm>[0-5]\d)\s*-\s*(?P<eh>[01]\d|2[0-3]):(?P<em>[0-5]\d)$")

class LocationForm(forms.ModelForm):
    """Form for creating/editing Locations with custom validation.

    Notes:
    - Address is required and must not be empty or whitespace only.
    - Working hours must follow the format "HH:MM - HH:MM".
    - Timezone is required and must be a valid timezone string.
    """
    class Meta:
        model = Location
        fields = ["role", "name", "address", "working_hours", "working_days", "timezone"]
        widgets = {
            "role": forms.Select(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Location Name"}),
            "address": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Location Address"}),
            "working_hours": forms.TextInput(attrs={"class": "form-control", "placeholder": "HH:MM - HH:MM"}),
            "working_days": forms.Select(attrs={"class": "form-control"}, choices=[
                ("Monday-Friday", "Monday-Friday"),
                ("All Days", "All Days"),
            ]),
            "timezone": forms.Select(attrs={"class": "form-control"}, choices=[(tz, tz) for tz in sorted(available_timezones())]),
        }
        labels = {
            "role": "Role",
            "name": "Location Name",
            "address": "Location Address",
            "working_hours": "Working Hours",
            "Working_days": "Working Days",
            "timezone": "Timezone",
        }
        error_messages = {
            "role": {"required": "Role is required."},
            "name": {
                "required": "Location name is required.",
                "unique": "This location name already exists.",
            },
            "address": {"required": "Location address is required."},
            "working_hours": {"required": "Working hours are required."},
            "Working_days": {"required": "Working days are required."},
            "timezone": {"required": "Timezone is required."},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["role"].queryset = Role.objects.all().order_by("name")

    def clean_name(self):
        name = (self.cleaned_data.get("name") or "").strip()
        if not name:
            raise ValidationError("Location name cannot be empty.")
        if not NAME_PATTERN.fullmatch(name):
            raise ValidationError(
                "Invalid name. Allowed: letters, digits, spaces, - _ . & ( ), 2–100 chars."
            )
        return name

    def clean_address(self):
        address = (self.cleaned_data.get("address") or "").strip()
        if not address:
            raise ValidationError("Address cannot be empty or whitespace.")
        return address

    def clean_working_hours(self):
        raw = (self.cleaned_data.get("working_hours") or "").strip()
        if not raw:
            raise ValidationError("Working hours are required.")
        m = WORKING_HOURS_PATTERN.fullmatch(raw)
        if not m:
            raise ValidationError("Format must be HH:MM - HH:MM (24h).")
        sh, sm, eh, em = map(int, (m.group("sh"), m.group("sm"), m.group("eh"), m.group("em")))
        start = time(sh, sm)
        end = time(eh, em)
        if start >= end:
            raise ValidationError("Start time must be earlier than end time.")
        # Normalize formatting
        return f"{start.strftime('%H:%M')} - {end.strftime('%H:%M')}"

    def clean_timezone(self):
        tz = (self.cleaned_data.get("timezone") or "").strip()
        if not tz:
            raise ValidationError("Timezone is required.")
        if tz not in available_timezones():
            raise ValidationError("Invalid timezone selected.")
        return tz
    def clean_Working_days(self):
        working_days = (self.cleaned_data.get("Working_days") or "").strip()
        if not working_days:
            raise ValidationError("Working days are required.")
        if working_days not in ["Monday-Friday", "All Days"]:
            raise ValidationError("Invalid working days selection.")
        return working_days
    
    def clean(self):
        cleaned_data = super().clean()
        # Additional cross-field validation can be added here if needed
        if Location.objects.filter(
            role=cleaned_data.get("role"),
            name=cleaned_data.get("name"),
            working_hours=cleaned_data.get("working_hours"),
            working_days=cleaned_data.get("working_days"),
            timezone=cleaned_data.get("timezone")
        ).exclude(id=self.instance.id if self.instance else None).exists():
            self.add_error("name", "This location already exists.")
        return cleaned_data

    def save(self, commit=True):
        return super().save(commit)
    