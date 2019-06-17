from django.db import models
# Create your models here.
class Employeet(models.Model):
    GENDER =(('M','Male'),('F','Female'),('O','Other'),('N','NA'))
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,choices= GENDER)
    date_of_birth = models.DateField()
    email_id = models.EmailField()
    mobile_number = models.IntegerField()
    address = models.CharField(max_length=300)
    aadhar_no = models.IntegerField()
    #--------------------------------------------
    bank_account_name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=15)
    account_number = models.IntegerField()
    def get_absolute_url(self):
        return "/empdet/employee/display/%i" %self.id
    
    attr_list=['First name', 'Middle name', 'Last Name', 'Gender', 
               'Date of Birth', 'Email id', 'Mobile Number', 'Address', 
               'Aadhar Number', 'Bank Account Name', 'IFSC', 'Acc num']
    def attr_list(self,a):
        return self.attr_list[a-1]