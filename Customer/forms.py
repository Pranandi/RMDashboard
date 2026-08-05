import django.forms as forms  # type: ignore
from .models import Customer
import re

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ["name", "contact_person_name", "contact_person_email", "contact_person_phone", "confluence_page_link", "customer_webpage", "customer_logo"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Customer Name"}),
            "contact_person_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Contact Person Name"}),
            "contact_person_email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Contact Person Email"}),
            "contact_person_phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Contact Person Phone"}),
            "confluence_page_link": forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter Confluence Page Link"}),
            "customer_webpage": forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter Customer Webpage"}),
            "customer_logo": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        }
        labels = {
            "name": "Customer Name",
            "contact_person_name": "Contact Person Name",
            "contact_person_email": "Contact Person Email",
            "contact_person_phone": "Contact Person Phone",
            "confluence_page_link": "Confluence Page Link",
            "customer_webpage": "Customer Webpage",
            "customer_logo": "Customer Logo",            
        }
        error_messages = {
            "name": {
                "required": "Customer name is required.",
                "unique": "This customer name already exists.",
            },
            "contact_person_name": {
                "required": "Contact person name is required.",
            },
            "contact_person_email": {
                "required": "Contact person email is required.",
                "invalid": "Enter a valid email address.",
            },
            "contact_person_phone": {
                "invalid": "Enter a valid phone number.",
            },
            "confluence_page_link": {
                "invalid": "Enter a valid URL.",
            },
            "customer_webpage": {
                "invalid": "Enter a valid URL.",
            },
            "customer_logo": {
                "invalid": "Upload a valid image file.",
                "filetype": "Unsupported file type.",
            },
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name:
            raise forms.ValidationError("Customer name cannot be empty.")
        if name and name.strip() == "":
            raise forms.ValidationError("Customer name cannot be just whitespace.")
        if name and re.search(r"\d", name):
            raise forms.ValidationError("Customer name must not contain numbers.")
        return name

    def clean_contact_person_name(self):
        contact_name = self.cleaned_data.get("contact_person_name")
        if not contact_name:
            raise forms.ValidationError("Contact person name cannot be empty.")
        if contact_name and contact_name.strip() == "":
            raise forms.ValidationError("Contact person name cannot be just whitespace.")
        if contact_name and re.search(r"\d", contact_name):
            raise forms.ValidationError("Contact person name must not contain numbers.")
        return contact_name
    
    def clean_contact_person_email(self):
        email = self.cleaned_data.get("contact_person_email")
        if not email:
            raise forms.ValidationError("Contact person email cannot be empty.")
        return email

    def clean_contact_person_phone(self):
        phone = self.cleaned_data.get("contact_person_phone")
        if not phone:
            raise forms.ValidationError("Contact person phone cannot be empty.")
        phone_pattern = re.compile(r'^\+?1?\d{9,15}$')
        if not phone_pattern.match(phone):
            raise forms.ValidationError('Enter a valid phone number.')
        return phone

    def clean_confluence_page_link(self):
        link = self.cleaned_data.get("confluence_page_link")
        if link and re.compile(r'^(https)://[^\s/$.?#].[^\s]*$').match(link) is None:
            raise forms.ValidationError("Enter a valid URL.")
        return link

    def clean_customer_webpage(self):
        webpage = self.cleaned_data.get("customer_webpage")
        if webpage and re.compile(r'^(https)://[^\s/$.?#].[^\s]*$').match(webpage) is None:
            raise forms.ValidationError("Enter a valid URL.")
        return webpage
    
    def clean_customer_logo(self):
        logo = self.cleaned_data.get("customer_logo")
        if logo:
            valid_mime_types = ['image/jpeg', 'image/png', 'image/gif']
            content_type = getattr(logo, 'content_type', None)
            if content_type is None and hasattr(logo, 'file'):
                content_type = getattr(logo.file, 'content_type', None)

            # Fallback: guess from filename if content_type is missing (e.g., BytesIO in tests)
            if content_type is None and hasattr(logo, 'name'):
                import mimetypes
                content_type, _ = mimetypes.guess_type(getattr(logo, 'name', ''))

            # Last-resort: quick signature sniff without external deps
            if content_type is None and hasattr(logo, 'file') and hasattr(logo.file, 'read'):
                f = logo.file
                try:
                    pos = f.tell()
                except Exception:
                    pos = None
                try:
                    head = f.read(10) or b''
                finally:
                    try:
                        if pos is not None:
                            f.seek(pos)
                    except Exception:
                        pass
                if head.startswith(b'\x89PNG\r\n\x1a\n'):
                    content_type = 'image/png'
                elif head.startswith(b'\xff\xd8'):
                    content_type = 'image/jpeg'
                elif head[:6] in (b'GIF87a', b'GIF89a'):
                    content_type = 'image/gif'

            if content_type and content_type not in valid_mime_types:
                raise forms.ValidationError("Unsupported file type.")
        return logo
    
    def save(self, commit: bool = True):
        customer = super().save(commit=False)
        if commit:
            customer.save()
        return customer
