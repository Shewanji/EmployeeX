from django import forms
from .models import Employee
from django.core.exceptions import ValidationError

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'hire_date', 'address', 'department', 'role']

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        super(EmployeeForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if self.instance and self.instance.email == email:
            return email  # Skip uniqueness check if email hasn't changed

        if Employee.objects.filter(email=email).exists():
            raise ValidationError('This email address is already in use. Please enter a different email address.')
        return email

