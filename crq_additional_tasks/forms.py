import django.forms as forms  # type: ignore
from .models import CrqAdditionalTask


class CrqAdditionalTaskForm(forms.ModelForm):
    class Meta:
        model = CrqAdditionalTask
        fields = ['task_name', 'summary', 'assignee']
        widgets = {
            'task_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Task Name"}),
            'summary': forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter Summary", "rows": 4}),
            'assignee': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Assignee"}),
        }
        labels = {
            'task_name': 'Task Name',
            'summary': 'Summary',
            'assignee': 'Assignee',
        }
        error_messages = {
            'task_name': {
                'required': 'Task Name is required.',
                'max_length': 'Task Name cannot exceed 100 characters.',
            },
            'assignee': {
                'required': 'Assignee is required.',
                'max_length': 'Assignee cannot exceed 100 characters.',
            },
        }
    def clean(self):
        cleaned_data = super().clean()
        task_name = cleaned_data.get('task_name')
        if task_name:
            cleaned_data['task_name'] = task_name.strip()
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
