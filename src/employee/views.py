from django.shortcuts import render
from django.views.generic.edit import CreateView
from employee.models import Employee

# Create your views here.
class EmployeeCreateView(CreateView):
    model = Employee
    fields = ('first_name','middle_name','last_name')
