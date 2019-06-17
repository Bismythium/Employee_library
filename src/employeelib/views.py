from django.views.generic.edit import CreateView,UpdateView
from .models import Employeet
from employeelib.forms import EmployeeForm
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
# Create your views here.
class EmployeeView(CreateView):
    model = Employeet
    fields = ('first_name','middle_name','last_name',
                  'gender','date_of_birth','email_id','mobile_number',
                  'address','aadhar_no', 'bank_account_name','ifsc_code',
                  'account_number')
    
class EmployeeUpdateView(UpdateView):
    model = Employeet
    form_class= EmployeeForm
    template_name= 'employeelib/employeet_update_form.html'
    
class EmployeeDetailView(DetailView):  
    def get(self,request,*args,**kwargs): #doubt!!
        form = EmployeeForm() 
        posts= Employeet.objects.all()
        catch = get_object_or_404(Employeet, pk=kwargs['pk']) 
        args={'form':form,'posts':posts,'catch':catch}
        return render(request, 'employeelib/employeet_detail.html' ,args)
        
