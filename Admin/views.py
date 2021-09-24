from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.contrib import messages
from .forms import AddAuthor
# Create your views here.
def Profile_admin(request):
    if request.user.is_superuser:
        return render(request, "Admin/admin_dashboard.html")
    else:
        return redirect(reverse('accounts:home')) 
def add_author(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            author_form = AddAuthor(request.POST)
            if author_form.is_valid():
                author_form.save()
                return redirect(reverse('Admin:admin_dashboard'))
            else:
                messages.error(request, 'Invalid data')
                return redirect(reverse('Admin:add_author'))
        else:
            author_form = AddAuthor()
            context = {'form': author_form}
            return render(request, "Books/add_author.html", context)
    else:
        return redirect(reverse('accounts:home')) 
