import django.forms as forms  # type: ignore
from .models import Role
import re

class RoleForm(forms.ModelForm):
    """Form for creating/editing Roles with custom validation.

    Notes:
    - Description is optional (model allows blank/null) but if provided it must NOT contain digits.
    - We still disallow strings that are only whitespace.
    """

    class Meta:
        model = Role
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Role Name"}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Role Description",
                    "rows": 4,
                }
            ),
        }
        labels = {
            "name": "Role Name",
            "description": "Role Description",
        }
        error_messages = {
            "name": {
                "required": "Role name is required.",
                "unique": "This role name already exists.",
            }
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name:
            raise forms.ValidationError("Role name cannot be empty.")
        if name and name.strip() == "":
            raise forms.ValidationError("Role name cannot be only whitespace.")
        if name and re.search(r"\d", name):
            raise forms.ValidationError("Role name must not contain numbers.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if description is None:
            return description  # allow null/blank per model if not provided
        # Normalize line breaks and trim
        if description.strip() == "":
            # Treat pure whitespace as empty (allowed) -> return empty string
            return ""
        # Reject any numeric characters
        if re.search(r"\d", description):
            raise forms.ValidationError("Description must not contain numbers.")
        return description
    
    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get("name")
        desc = cleaned_data.get("description")
        if role and desc and role.strip().lower() == desc.strip().lower():
            raise forms.ValidationError("Role name and description cannot be the same.")
        return cleaned_data

    def save(self, commit: bool = True):
        role = super().save(commit=False)
        if commit:
            role.save()
        return role
