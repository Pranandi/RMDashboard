import re
from django import forms  # type: ignore
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'code', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Project Name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Project Code' }),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Project Description', 'rows': 4}),
        }
        labels = {
            'name': 'Project Name',
            'code': 'Project Code',
            'description': 'Project Description',
        }
        error_messages = {
            'name': {
                'required': 'Project name is required.',
            },
            'code': {
                'required': 'Project code is required.',
                'unique': 'This project code already exists.'
            }
        }

    def clean_name(self):
        name = (self.cleaned_data.get('name') or '').strip()
        if not name:
            raise forms.ValidationError('Project name cannot be empty.')
        if name and not re.compile(r'^[A-Za-z ]+$').match(name):
            raise forms.ValidationError('Project name must be a letter and space.')
        return name

    def clean_code(self):
        code = (self.cleaned_data.get('code') or '').strip()
        if not code:
            raise forms.ValidationError('Project code cannot be empty.')
        if code.isalpha() and len(code) != 2:
            raise forms.ValidationError('Project code must be exactly 2 characters long.')
        elif code.isdigit() and int(code) <= 0:
            raise forms.ValidationError('Project code must be a positive number.')
        return code

    def clean_description(self):
        description = (self.cleaned_data.get('description') or '').strip()
        if not description:
            raise forms.ValidationError('Project description cannot be empty.')
        return description