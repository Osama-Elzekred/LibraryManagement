from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile
import phonenumbers
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'phone_number', 'gender', 'birthday', 'address']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'phone_number', 'gender', 'birthday', 'address']
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
