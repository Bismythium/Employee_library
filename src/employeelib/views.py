from django.shortcuts import render
from django.views.generic import DetailView,CreateView
from .models import Employee
# Create your views here.
class EmployeeView(CreateView):
    model = Employee
    fields = ('first_name','middle_name','last_name',
                  'gender','date_of_birth','email_id','mobile_number',
                  'address','aadhar_no', 'bank_account_name','ifsc_code',
                  'account_number')
    
    template_name= 'employeelib/enter_detail_form.html'

class EmployeeDisplayView(DetailView):
    template_name='employeelib/employee_display.html'
    model=Employee