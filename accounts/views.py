from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render 
from .forms import RegisterForm
from django.urls import reverse
# Create your views here.
def profile(request):
    return render(request, "profile.html")
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect(reverse('accounts:profile'))
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('accounts:profile'))
    else:
        form = RegisterForm()
    return render(request, 'register.html' , {'form':form})
