from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Siteuser

class SiteuserLoginForm(forms.ModelForm):
    class Meta:
        model = Siteuser
        fields = ('username','password')
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method='post'
        self.helper.add_input(Submit('Login','Log user'))
        
class SiteuserSignupForm(forms.ModelForm):
    class Meta:
        model = Siteuser
        fields= ('username','email_id','password','confirm_password')
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper =FormHelper()
        self.helper.form_method='post'
        self.helper.add_input(Submit('Signup','log user'))