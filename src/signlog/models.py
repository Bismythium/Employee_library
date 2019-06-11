from django.db import models

# Create your models here.
class Siteuser(models.Model):
    username= models.CharField(max_length=25, verbose_name='Username')
    password= models.CharField(max_length=30)
    confirm_password= models.CharField(max_length=30)
    email_id= models.EmailField()
    
    def __str__(self):
        return self.username