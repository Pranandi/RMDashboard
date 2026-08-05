import django.forms as forms

from Project.models import Project  # type: ignore
from .models import Version
import re

class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = ["project", "operation_system", "version", "policy_name", "manual_file_name", "manual_file_location", "confluence_page_link"]
        widgets = {
            "project": forms.Select(attrs={"class": "form-control"}),
            "operation_system": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Operation System"}),
            "version": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Version"}),
            "policy_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Policy Name"}),
            "manual_file_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Manual File Name"}),
            "manual_file_location": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Manual File Location"}),
            "confluence_page_link": forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter Confluence Page Link"}),
        }
        labels = {
            "project": "Project",
            "operation_system": "Operation System",
            "version": "Version",
            "policy_name": "Policy Name",
            "manual_file_name": "Manual File Name",
            "manual_file_location": "Manual File Location",
            "confluence_page_link": "Confluence Page Link",
            
        }
        error_messages = {
            "project": {
                "required": "Project is required.",
            },
            "operation_system": {
                "required": "Operation system is required.",
            },
            "version": {
                "required": "Version is required.",
            },
            "policy_name": {
                "required": "Policy name is required.",
                "unique": "This policy name already exists.",
            },
            "manual_file_name": {
                "required": "Manual file name is required.",
            },
            "manual_file_location": {
                "required": "Manual file location is required.",
            },
            "confluence_page_link": {
                "invalid": "Enter a valid URL.",
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.all().order_by('name')
        
    def clean_project(self):
        project = self.cleaned_data.get("project")
        if not project:
            raise forms.ValidationError("Project cannot be empty.")
        return project

    def clean_operation_system(self):
        os = self.cleaned_data.get("operation_system")
        if not os:
            raise forms.ValidationError("Operation system cannot be empty.")
        if os and os.strip() == "":
            raise forms.ValidationError("Operation system cannot be just whitespace.")
        return os
    
    def clean_version(self):
        version = self.cleaned_data.get("version")
        if not version:
            raise forms.ValidationError("Version cannot be empty.")
        if version and version.strip() == "":
            raise forms.ValidationError("Version cannot be just whitespace.")
        if version and not re.compile(r'^[0-9]+(\.[0-9]+)*$').match(version):
            raise forms.ValidationError("Version must be in the format 'X.Y.Z' where X, Y, and Z are numbers.")
        return version
    
    def clean_policy_name(self):
        policy_name = self.cleaned_data.get("policy_name")
        if not policy_name:
            raise forms.ValidationError("Policy name cannot be empty.")
        if policy_name and policy_name.strip() == "":
            raise forms.ValidationError("Policy name cannot be just whitespace.")
        return policy_name
    
    def clean_manual_file_name(self):
        name = self.cleaned_data.get("manual_file_name")
        if not name:
            raise forms.ValidationError("Manual file name cannot be empty.")
        if name and name.strip() == "":
            raise forms.ValidationError("Manual file name cannot be just whitespace.")
        if name and not (name.endswith('.exe') or name.endswith('.msi') or name.endswith('.zip')):
            raise forms.ValidationError("Manual file name must end with .exe, .msi, or .zip.")
        return name
    
    def clean_manual_file_location(self):
        location = self.cleaned_data.get("manual_file_location")
        if not location:
            raise forms.ValidationError("Manual file location cannot be empty.")
        if location and location.strip() == "":
            raise forms.ValidationError("Manual file location cannot be just whitespace.")
        return location

    def clean_confluence_page_link(self):
        link = self.cleaned_data.get("confluence_page_link")
        if not link:
            raise forms.ValidationError("Confluence page link cannot be empty.")
        if link and not re.compile(r'^(https?)://[^\s/$.?#].[^\s]*$').match(link):
            raise forms.ValidationError("Enter a valid URL.")
        return link

    def save(self, commit: bool = True):
        customer = super().save(commit=False)
        if commit:
            customer.save()
        return customer
