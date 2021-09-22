from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render 
from .forms import UserRegisterForm , ProfileRegisterForm , UserUpdateForm , ProfileUpdateForm
from django.views import View
from django.urls import reverse
# Create your views here.
class SignUp(View):

    def get (self, request, *args, **kwargs):
        user_form = UserRegisterForm()
        profile_form = ProfileRegisterForm()
        context = {'user_form':user_form, 'profile_form':profile_form}
        return render(request, "register.html", context)
    
    def post (self, request, *args, **kwargs):
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileRegisterForm(request.POST , request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            user = authenticate(username = user_form.cleaned_data.get('username') , password = user_form.cleaned_data.get('password1'))
            profile_form.custom_save(user=user)
        return redirect(reverse('accounts:profile'))

class UpdateData(View):
    def get (self, request, *args, **kwargs):
        user_form = UserUpdateForm()
        profile_form = ProfileUpdateForm()
        context = {'user_form':user_form, 'profile_form':profile_form}
        return render(request, 'profile.html', context)

    def post(self, request, *args, **kwargs):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            redirect(reverse('accounts:profile'))

def sign_up(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            redirect(reverse('accounts:profile'))
            
    else:
        form = UserRegisterForm()
    return render(request, 'register.html' , {'form':form})


