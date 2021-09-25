from Books.models import Category
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render 
from .forms import UserRegisterForm , ProfileRegisterForm , UserUpdateForm , ProfileUpdateForm
from django.views import View
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
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
    def post(self, request, *args, **kwargs):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile Data has been updated successfully!')
            return redirect(reverse('accounts:profile'))
        else:
            messages.error(request, f'Invalid Date, Please Try Again!')
            return redirect(reverse('accounts:profile'))
    def get (self, request, *args, **kwargs):
        user_form = UserUpdateForm()
        profile_form = ProfileUpdateForm()
        profile = request.user.user_profile
        books = request.user.user_books.all()
        categories = Category.objects.all()
        context = {'user_form':user_form, 'profile_form':profile_form, 'profile':profile, 'Books':books, 'Categories':categories}
        return render(request, 'profile.html', context)


class ContactUs(View):
    def post (self, request, *args, **kwargs):
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['message']
        send_mail (
            subject,
            msg,
            settings.EMAIL_HOST_USER,
            [email],
        )
        return redirect(reverse('contact'))
    def get (self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'contact_us.html',{'Categories':categories})

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



