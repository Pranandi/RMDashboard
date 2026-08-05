import re
import django.forms as forms # type: ignore
from django.db import models  # for Q lookups in EmployeeLoginForm
from django.db.models import Min  # for getting minimum id per location in EmployeeForm
from datetime import date

from .models import Employee
from Role.models import Role  # import the Role model class
from Location.models import Location  # import the Location model class


class EmployeeForm(forms.ModelForm):
    # Non-model field for confirmation only
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm the Password'}),
        required=True
    )

    class Meta:
        model = Employee
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'role', 'cuid',
            'employee_code', 'location', 'designation', 'is_active', 'hired_date', 'manager_name', 'password'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the First Name'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Last Name'}),
            'email'     : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter the Email'}),
            'phone'     : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the Phone Number'}),
            'cuid'      : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the CUID'}),
            'employee_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the Employee Code', 'maxlength':'6'}),
            'designation': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the Designation'}),
            'is_active' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'hired_date': forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'password'  : forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter the Password'}),
            'confirm_password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm the Password'}),
            # QuerySets should not be evaluated at import time; override in __init__ for fresh data.
            'role'      : forms.Select(attrs={'class':'form-control'}),
            'location'  : forms.Select(attrs={'class':'form-control'}),
            'manager_name'   : forms.Select(attrs={'class':'form-control'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone': 'Phone Number',
            'role': 'Role',
            'cuid': 'CUID',
            'employee_code': 'Employee Code',
            'location': 'Location',
            'designation': 'Designation',
            'is_active': 'Is Active',
            'hired_date': 'Hired Date',
            'manager_name': 'Manager Name',
            'password': 'Password',
        }
        error_messages = {
            'first_name': {
                'required': 'First name is required.',
            },
            'last_name': {
                'required': 'Last name is required.',
            },
            'email': {
                'required': 'Email is required.',
                'invalid': 'Enter a valid email address.',
            },
            'phone': {
                'required': 'Phone number is required.',
                'invalid': 'Enter a valid phone number.',
            },
            'role': {
                'required': 'Role is required.',
            },
            'cuid': {
                'required': 'CUID is required.',
            },
            'employee_code': {
                'required': 'Employee Code is required.',
            },
            'location': {
                'required': 'Location is required.',
            },
            'designation': {
                'required': 'Designation is required.',
            },
            'is_active': {
                'required': 'Is Active is required.',
            },
            'hired_date': {
                'required': 'Hired Date is required.',
            },
            'manager_name': {
                'required': 'Manager Name is required.',
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically set choices so they reflect current DB state and avoid import-time queries
        self.fields['hired_date'].widget.attrs['max'] = date.today().isoformat()
        self.fields['role'].queryset = Role.objects.all().order_by('name')
        unique_ids = (
            Location.objects
            .values('name')
            .annotate(min_id=Min('id'))
            .values_list('min_id', flat=True)
        )
        self.fields['location'].queryset = Location.objects.filter(id__in=list(unique_ids)).order_by('name')
        if self.instance.pk:
            print("Editing existing employee, excluding self from manager choices.")
            managers = Employee.objects.filter(manager_name=self.instance.pk)
            self.fields['manager_name'].queryset = Employee.objects.exclude(id__in=managers).exclude(id=self.instance.pk).order_by('first_name', 'last_name')
        else:
            self.fields['manager_name'].queryset = Employee.objects.all().order_by('first_name', 'last_name')

        # If editing an existing employee, remove password fields so they cannot be changed here
        if self.instance.pk:
            # Prevent unintended password overwrite by removing password-related fields
            self.fields.pop('password', None)
            self.fields.pop('confirm_password', None)

    # Validation methods (correctly scoped on the form class)
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name', '')
        if not re.compile(r'^[A-Za-z ]+$').match(first_name):
            raise forms.ValidationError('First name should only contain alphabetic characters.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name', '')
        if not last_name.isalpha():
            raise forms.ValidationError('Last name should only contain alphabetic characters.')
        return last_name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        phone_pattern = re.compile(r'^\+?1?\d{9,15}$')
        if not phone_pattern.match(phone):
            raise forms.ValidationError('Enter a valid phone number.')
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Employee.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Email already exists.')
        #if email and not email.endswith('@lumen.com'):
        #    raise forms.ValidationError('Please use a Lumen email address.')
        return email

    def clean_employee_code(self):
        code = self.cleaned_data.get('employee_code')
        if code and Employee.objects.filter(employee_code__iexact=code).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Employee code already exists.')
        if code and not code.isdigit():
            raise forms.ValidationError('Employee code should be entirely numeric.')
        if code and len(code) != 6:
            raise forms.ValidationError('Employee code must be exactly 6 digits long.')
        return code

    def clean_cuid(self):
        cuid = self.cleaned_data.get('cuid')
        if cuid:
            if Employee.objects.filter(cuid__iexact=cuid).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('CUID already exists.')
            # Validate format: 2 letters followed by 5 digits (e.g., AA12345)
            cuid_pattern = re.compile(r'^[A-Z]{2}\d{5}$')
            if not cuid_pattern.match(cuid):
                raise forms.ValidationError('CUID must be 2 letters followed by 5 digits (e.g., AA12345).')
        return cuid

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and self.instance.pk is None:  # Only enforce on new records or when password is provided
            if len(password) < 12:
                raise forms.ValidationError('Password must be at least 12 characters long.')
            if not any(c.isdigit() for c in password):
                raise forms.ValidationError('Password must contain at least one digit.')
            if not any(c.isupper() for c in password):
                raise forms.ValidationError('Password must contain at least one uppercase letter.')
            if not any(c.islower() for c in password):
                raise forms.ValidationError('Password must contain at least one lowercase letter.')
            if not any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for c in password):
                raise forms.ValidationError('Password must contain at least one special character.')
        return password

    def clean(self):
        cleaned = super().clean()
        if self.instance.pk is None:  # Only enforce on new records
            pwd = cleaned.get('password')
            confirm = cleaned.get('confirm_password')
            if pwd and confirm and pwd != confirm:
                self.add_error('confirm_password', 'Passwords do not match.')
        return cleaned

    def save(self, commit=True):
        """Override save to hash password if it's in plain text.

        Softly migrates existing plaintext passwords: if the current instance
        already has a hashed password and no new password provided, it keeps it.
        """
        instance = super().save(commit=False)
        if self.instance.pk is None:  # Only hash password for new records
            from django.contrib.auth.hashers import make_password # type: ignore
            pwd = self.cleaned_data.get('password')
            # Heuristic: Django hashed passwords contain a '$' separator (e.g., 'pbkdf2_sha256$...')
            if pwd and '$' not in pwd:
                instance.password = make_password(pwd)
        if commit:
            instance.save()
        return instance


class EmployeeLoginForm(forms.Form):
    identifier = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email or CUID or Employee Code'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    labels = {
        'identifier': 'Email or CUID or Employee Code',
        'password': 'Password',
    }
    def clean_identifier(self):
        identifier = self.cleaned_data.get('identifier', '').strip()
        if not identifier:
            raise forms.ValidationError('This field is required.')
        # should check on Employee
        if not Employee.objects.filter(
            models.Q(email__iexact=identifier) |
            models.Q(cuid__iexact=identifier) |
            models.Q(employee_code__iexact=identifier)
        ).exists():
            raise forms.ValidationError('No employee found with this identifier.')
        return identifier
    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if not password:
            raise forms.ValidationError('This field is required.')
        return password

class EmployeeForgotForm(forms.Form):
    cuid = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your CUID'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}))
    employee_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Employee Code'}))
    
    labels ={
        'cuid' : 'CUID',
        'email' : 'Email',
        'employee_code' : 'Employee Code',
    }
    
    def clean_cuid(self):
        cuid = self.cleaned_data.get('cuid', '').strip()
        if not cuid:
            raise forms.ValidationError('This field is required.')
        if cuid and not Employee.objects.filter(cuid__iexact=cuid).exists():
            raise forms.ValidationError('No employee found with this CUID.')
        return cuid

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip()
        if not email:
            raise forms.ValidationError('This field is required.')
        if email and not Employee.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('No employee found with this Email.')
        return email

    def clean_employee_code(self):
        employee_code = self.cleaned_data.get('employee_code', '').strip()
        if not employee_code:
            raise forms.ValidationError('This field is required.')
        if employee_code and not Employee.objects.filter(employee_code__iexact=employee_code).exists():
            raise forms.ValidationError('No employee found with this Employee Code.')
        return employee_code
    
    def clean(self):
        cleaned = super().clean()
        cuid = cleaned.get('cuid')
        email = cleaned.get('email')
        employee_code = cleaned.get('employee_code')
        if cuid and email and employee_code:
            if not Employee.objects.filter(
                cuid__iexact=cuid,
                email__iexact=email,
                employee_code__iexact=employee_code
            ).exists():
                raise forms.ValidationError('The provided CUID, Email, and Employee Code do not match any employee.')
        return cleaned

class EmployeeResetForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new Password'}))
    token = forms.CharField(widget=forms.HiddenInput())
    
    labels = {
        'password': 'New Password',
        'confirm_password': 'Confirm New Password',
    }
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            if len(password) < 12:
                raise forms.ValidationError('Password must be at least 12 characters long.')
            if not any(c.isdigit() for c in password):
                raise forms.ValidationError('Password must contain at least one digit.')
            if not any(c.isupper() for c in password):
                raise forms.ValidationError('Password must contain at least one uppercase letter.')
            if not any(c.islower() for c in password):
                raise forms.ValidationError('Password must contain at least one lowercase letter.')
            if not any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for c in password):
                raise forms.ValidationError('Password must contain at least one special character.')
        return password
    
    def clean(self):
        cleaned = super().clean()
        pwd = cleaned.get('password')
        confirm = cleaned.get('confirm_password')
        if pwd and confirm and pwd != confirm:
            self.add_error('confirm_password', 'Passwords do not match.')
        return cleaned
    
    def clean_token(self):
        token = self.cleaned_data.get('token', '').strip()
        if not token:
            raise forms.ValidationError('Invalid or missing token.')
        return token

class EmployeeChangePasswordForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter current Password'}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new Password'}))
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new Password'}))
    
    labels = {
        'current_password': 'Current Password',
        'new_password': 'New Password',
        'confirm_new_password': 'Confirm New Password',
    }
    def clean_current_password(self):
        password = self.cleaned_data.get('current_password', '')
        if not password:
            raise forms.ValidationError('This field is required.')
        return password
    def clean_new_password(self):
        password = self.cleaned_data.get('new_password')
        if password:
            if len(password) < 12:
                raise forms.ValidationError('Password must be at least 12 characters long.')
            if not any(c.isdigit() for c in password):
                raise forms.ValidationError('Password must contain at least one digit.')
            if not any(c.isupper() for c in password):
                raise forms.ValidationError('Password must contain at least one uppercase letter.')
            if not any(c.islower() for c in password):
                raise forms.ValidationError('Password must contain at least one lowercase letter.')
            if not any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for c in password):
                raise forms.ValidationError('Password must contain at least one special character.')
        return password
    
    def clean(self):
        cleaned = super().clean()
        new_pwd = cleaned.get('new_password')
        confirm = cleaned.get('confirm_new_password')
        if new_pwd and confirm and new_pwd != confirm:
            self.add_error('confirm_new_password', 'Passwords do not match.')
        return cleaned