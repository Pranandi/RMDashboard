import django.forms as forms # type: ignore

from .models import ContactUs
import re

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["name","title","email","phone","alternative_phone"]
        widgets = {
           "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Employee Name"})   ,
           "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Title"}),
           "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Your Email"}),
           "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Your Phone Number"}),
           "alternative_phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Alternative Phone Number"}),
        }
        labels = {
              "name": "Employee Name",
              "title": "Title",
              "email": "Email",
              "phone": "Phone Number",
              "alternative_phone": "Alternative Phone Number",
        }
        error_messages = {
            "name": {
                "required": "Employee name is required.",
            },
            "title": {
                "required": "Title is required.",
            },
            "email": {
                "required": "Email is required.",
                "invalid": "Enter a valid email address.",
            },
            "phone": {
                "required": "Phone number is required.",
                "invalid": "Enter a valid phone number.",
            },
            "alternative_phone": {
                "invalid": "Enter a valid alternative phone number.",
            },
        }

    def clean_title(self):
        title = (self.cleaned_data.get('title') or '').strip()
        if not title:
            raise forms.ValidationError('Title cannot be empty.')
        if title and not re.compile(r'^[A-Za-z ]+$').match(title):
            raise forms.ValidationError('Title must contain only letters and spaces.')
        return title
    
    def clean_phone(self):
        phone = (self.cleaned_data.get('phone') or '').strip()
        if not phone:
            raise forms.ValidationError('Phone number cannot be empty.')
        # Simple regex for phone number validation (customize as needed)
        phone_pattern = re.compile(r'^\+?1?\d{9,15}$')
        if not phone_pattern.match(phone):
            raise forms.ValidationError('Enter a valid phone number.')
        return phone
    
    def clean_alternative_phone(self):
        alternative_phone = (self.cleaned_data.get('alternative_phone') or '').strip()
        if alternative_phone:
            # Simple regex for phone number validation (customize as needed)
            phone_pattern = re.compile(r'^\+?1?\d{9,15}$')
            if not phone_pattern.match(alternative_phone):
                raise forms.ValidationError('Enter a valid alternative phone number.')
        return alternative_phone
    
    def save(self, commit: bool = True):
        contact_us = super().save(commit=False)
        if commit:
            contact_us.save()
        return contact_us