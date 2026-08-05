import django.forms as forms  # type: ignore
from .models import Clients

class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['client_name', 'vantive_name', 'site_id', 'advanced_essential', 'start_week', 'start_day', 'specific_date', 'frequency', 'add_month', 'notes', 'ask_for_approval_in_email', 'email_greeting', 'email_to', 'email_cc', 'email_bcc', 'is_active']
        widgets = {
            'client_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Client Name"}),
            'vantive_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Vantive Name"}),
            'site_id': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Site ID"}),
            'advanced_essential': forms.Select(attrs={"class": "form-control"}, choices=['Advanced', 'Essential']),
            'start_week': forms.Select(attrs={"class": "form-control"}, choices=['First', 'Second', 'Third', 'Fourth','Penultimate','Last','Specific Date','First Weekday']),
            'start_day' : forms.Select(attrs={"class": "form-control"}, choices=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','Specific Date','First Weekday']),
            'specific_date': forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            'frequency' : forms.Select(attrs={"class": "form-control"}, choices=['Monthly','Bi-Monthly','Quarterly','Request']),
            'add_month': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Add Month"}),
            'notes': forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter Notes", "rows": 4}),
            'ask_for_approval_in_email': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'email_greeting': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Email Greeting"}),
            'email_to': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Email To (separate multiple emails with commas)"}),
            'email_cc': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Email CC (separate multiple emails with commas)"}),
            'email_bcc': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Email BCC (separate multiple emails with commas)"}),
            'is_active': forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {
            'client_name': 'Client Name',
            'vantive_name': 'Vantive Name',
            'site_id': 'Site ID',
            'advanced_essential': 'Advanced/Essential',
            'start_week': 'Start Week',
            'start_day': 'Start Day',
            'specific_date': 'Specific Date',
            'frequency': 'Frequency',
            'add_month': 'Add Month',
            'notes': 'Notes',
            'ask_for_approval_in_email': 'Ask for approval in email',
            'email_greeting': 'Email Greeting',
            'email_to': 'Email To',
            'email_cc': 'Email CC',
            'email_bcc': 'Email BCC',
            'is_active': 'Is Active',
        }
        error_messages = {
            'client_name': {
                'required': 'Client Name is required.',
                'max_length': 'Client Name cannot exceed 100 characters.'
            },
            'vantive_name': {
                'required': 'Vantive Name is required.',
                'max_length': 'Vantive Name cannot exceed 100 characters.'
            },
            'site_id': {
                'required': 'Site ID is required.',
                'max_length': 'Site ID cannot exceed 100 characters.'
            },
            'add_month': {
                'max_length': 'Add Month cannot exceed 20 characters.'
            },
            'email_greeting': {
                'max_length': 'Email Greeting cannot exceed 255 characters.'
            },
            'email_to': {
                'max_length': 'Email To cannot exceed 255 characters.'
            },
            'email_cc': {
                'max_length': 'Email CC cannot exceed 255 characters.'
            },
            'email_bcc': {
                'max_length': 'Email BCC cannot exceed 255 characters.'
            },
        }
    
    def clean(self):
        cleaned_data = super().clean()
        start_week = cleaned_data.get('start_week')
        start_day = cleaned_data.get('start_day')
        specific_date = cleaned_data.get('specific_date')
        email_to = cleaned_data.get('email_to')
        email_cc = cleaned_data.get('email_cc')
        email_bcc = cleaned_data.get('email_bcc')
        
        if (start_week == 'Specific Date' or start_day == 'Specific Date') and not specific_date:
            raise forms.ValidationError('Specific Date is required when Start Week or Start Day is set to Specific Date.')
        
        if email_to and not self.validate_email_list(email_to):
            raise forms.ValidationError('Email To field contains invalid email addresses.')
        if email_cc and not self.validate_email_list(email_cc):
            raise forms.ValidationError('Email CC field contains invalid email addresses.')
        if email_bcc and not self.validate_email_list(email_bcc):
            raise forms.ValidationError('Email BCC field contains invalid email addresses.')
        return cleaned_data
    
    def validate_email_list(self, email_list):
        emails = [email.strip() for email in email_list.split(',')]
        for email in emails:
            try:
                forms.EmailField().clean(email)
            except forms.ValidationError:
                return False
        return True
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
            
            