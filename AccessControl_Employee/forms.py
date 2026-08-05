import django.forms as forms
from Employee.models import Employee
from .models import AccessControl_Employee
from django.apps import apps

MENU_CHOICES = [
    (app.name, app.verbose_name.replace('_', ' ').title()) for app in apps.get_app_configs() if not app.name.startswith('django.')
]

class AccessControlEmployeeForm(forms.ModelForm):
    # Multi-select of app names
    app_name = forms.MultipleChoiceField(
        choices=MENU_CHOICES,
        required=True,
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        label="Menus"
    )

    class Meta:
        model = AccessControl_Employee
        # Keep app_name in fields so form renders it; we will override save
        fields = ["employee", "app_name", "can_view", "can_add", "can_edit", "can_delete", "can_export"]
        widgets = {
            "employee": forms.Select(attrs={"class": "form-control"}),
            "app_name": forms.SelectMultiple(attrs={"class": "form-control"}),
            "can_view": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "can_add": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "can_edit": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "can_delete": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "can_export": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {
            "employee": "Employee",
            "app_name": "Menus",
            "can_view": "Can View",
            "can_add": "Can Add",
            "can_edit": "Can Edit",
            "can_delete": "Can Delete",
            "can_export": "Can Export",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["employee"].queryset = Employee.objects.order_by("first_name", "last_name")

    def clean_app_name(self):
        vals = self.cleaned_data.get("app_name") or []
        # dedupe preserving order
        return [v for i, v in enumerate(vals) if v not in vals[:i]]

    def clean(self):
        cleaned = super().clean()
        # No per-row uniqueness check here; we will skip existing rows in save
        return cleaned

    def save(self, commit=True):
        """
        Create one row per selected menu.
        Return list of created objects (and skip ones that already exist).
        """
        employee = self.cleaned_data["employee"]
        menus = self.cleaned_data["app_name"]  # list
        flags = {
            "can_view": self.cleaned_data.get("can_view", False),
            "can_add": self.cleaned_data.get("can_add", False),
            "can_edit": self.cleaned_data.get("can_edit", False),
            "can_delete": self.cleaned_data.get("can_delete", False),
            "can_export": self.cleaned_data.get("can_export", False),
        }
        created = []
        if commit:
            existing_names = set(
                AccessControl_Employee.objects.filter(employee=employee, app_name__in=menus)
                .values_list("app_name", flat=True)
            )
            for name in menus:
                if name in existing_names and not (self.instance.pk):
                    continue
                obj = AccessControl_Employee(employee=employee, app_name=name, **flags)
                obj.save()
                created.append(obj)
        return created

class AccessControlEmployeeEditForm(forms.ModelForm):
    class Meta:
        model = AccessControl_Employee
        fields = ["employee", "app_name", "can_view", "can_add", "can_edit", "can_delete", "can_export"]
        widgets = {
            "employee": forms.Select(attrs={"class": "form-control"}),
            "app_name": forms.Select(attrs={"class": "form-control"}),
            "can_view": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "can_add": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "can_edit": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "can_delete": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "can_export": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {
            "employee": "Employee",
            "app_name": "Menu",
            "can_view": "Can View",
            "can_add": "Can Add",
            "can_edit": "Can Edit",
            "can_delete": "Can Delete",
            "can_export": "Can Export",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["employee"].queryset = Employee.objects.order_by("first_name", "last_name")
        self.fields["app_name"].widget.choices = MENU_CHOICES
    
    def clean(self):
        cleaned = super().clean()
        employee = cleaned.get("employee")
        app_name = cleaned.get("app_name")
        if AccessControl_Employee.objects.filter(employee=employee, app_name=app_name).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This employee already has access settings for the selected menu.")
        return cleaned