from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pics", height_field=100, width_field=100)
    phone_number = PhoneNumberField(blank=1,null=1,max_length=11)
    gender = models.CharField(max_length=2,choices=(('M' , 'Male') , ('F' , 'Female')))
    birthday = models.DateField(null=1,blank=1)
    address = models.CharField(max_length=300, null=1, blank=1)
    


