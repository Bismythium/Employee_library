from django.db import models
# Create your models here.
class Employee(models.Model):
    GENDER =(('M','Male'),('F','Female'),('O','Other'),('N','NA'))
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
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