import django.forms as forms # type: ignore

from Employee.models import Employee
from Location.models import Location  # type: ignore
from django.db.models import Min
from .models import CoordinationAndExecutionEscalation
import re


CONTACT_TYPE_CHOICES = [
    ('Email', 'Email'),
    ('Teams', 'Teams'),
    ('Phone', 'Phone'),
]

class CoordinationAndExecutionEscalationForm(forms.ModelForm):

    # Override contact_type to allow multi-select (stored comma-separated in CharField)
    contact_type = forms.MultipleChoiceField(
        choices=CONTACT_TYPE_CHOICES,
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        label="Contact Type",
        required=True,
        help_text="Hold Ctrl/Cmd to select multiple."
    )

    employees = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.none(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        required=True,
        label="Employees"
    )

    class Meta:
        model = CoordinationAndExecutionEscalation
        fields = ["level", "description", "location", "employees", "contact_type"]
        widgets = {
            "level": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter Level"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter Description", "rows": 3}),
            "location": forms.Select(attrs={"class": "form-control"}),
            "contact_type": forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            "level": "Level",
            "description": "Description",
            "location": "Location",
            "employees": "Employees",
            "contact_type": "Contact Type",
        }
        error_messages = {
            "level": {
                "required": "Level is required.",
                "unique": "This level already exists.",
            },
            "description": {
                "required": "Description is required.",
            },
            "location": {
                "required": "Location is required.",
            },
            "employee": {
                "required": "Employee is required.",
            }
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically set choices so they reflect current DB state and avoid import-time queries
        unique_ids = (
            Location.objects
            .values('name')
            .annotate(min_id=Min('id'))
            .values_list('min_id', flat=True)
        )
        self.fields['location'].queryset = Location.objects.filter(id__in=list(unique_ids)).order_by('name')
        self.fields['employees'].queryset = Employee.objects.all().order_by('last_name')
        # Preselect existing employees when editing
        if self.instance and self.instance.pk:
            self.initial['employees'] = list(self.instance.employees.values_list('pk', flat=True))
        # Initialize multi-select from stored comma-separated string
        if self.instance and self.instance.pk and self.instance.contact_type:
            # Ensure previously saved comma-separated values show as selected
            existing = [v.strip() for v in self.instance.contact_type.split(',') if v.strip()]
            self.initial['contact_type'] = existing

    def clean_level(self):
        level = self.cleaned_data.get("level")
        if not level:
            raise forms.ValidationError("Level cannot be empty.")
        return level

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if not description:
            raise forms.ValidationError("Description cannot be empty.")
        return description

    def clean_location(self):
        location = self.cleaned_data.get("location")
        if not location:
            raise forms.ValidationError("Location cannot be empty.")
        return location

    def clean_employee(self):
        employee = self.cleaned_data.get("employee")
        if not employee:
            raise forms.ValidationError("Employee cannot be empty.")
        return employee

    def clean_contact_type(self):
        contact_types = self.cleaned_data.get("contact_type")
        if not contact_types:
            raise forms.ValidationError("Select at least one contact type.")
        # Validate choices already enforced by field; return normalized list
        return contact_types

    def clean_employees(self):
        employees = self.cleaned_data.get("employees")
        if not employees:
            raise forms.ValidationError("Select at least one employee.")
        return employees

    def save(self, commit: bool = True):
        escalation = super().save(commit=False)
        # store contact_type as comma-separated string
        contact_types = self.cleaned_data.get('contact_type', [])
        escalation.contact_type = ','.join(contact_types)
        if commit:
            escalation.save()
            # set M2M
            escalation.employees.set(self.cleaned_data['employees'])
        else:
            # when not committing, ensure instance has employees to set later
            self._pending_employees = self.cleaned_data['employees']
        return escalation
