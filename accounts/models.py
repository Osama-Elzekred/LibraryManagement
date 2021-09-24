from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image 
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_image = models.ImageField(upload_to="profile_pics",null=True, blank=True, default='default.jpg')
    phone_number = PhoneNumberField(region='EG',blank=True,null=True)
    gender = models.CharField(max_length=2,choices=(('M' , 'Male') , ('F' , 'Female')))
    birthday = models.DateField(null=1,blank=1)
    address = models.CharField(max_length=300, null=1, blank=1)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)
    #     if self.profile_image != None:
    #         img = Image.open(self.profile_image.path)
    #         if img.height > 300 or img.width > 300:
    #             new_size = (300, 300)
    #             img.thumbnail(new_size)
    #             img.save(self.profile_image.path)
    def custom_save(self, *args, **kwargs):
        self.user = kwargs.get('user')
        self.save()



