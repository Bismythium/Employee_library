from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from employee.models import Employee

class PersonForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name','middle_name','last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save employee'))