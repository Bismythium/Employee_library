from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name','middle_name','last_name',
                  'gender','date_of_birth','email_id','mobile_number',
                  'address','aadhar_no', 'bank_account_name','ifsc_code',
                  'account_number'
                  )
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method='post'
        self.helper.add_input(Submit('Store','Save user'))       