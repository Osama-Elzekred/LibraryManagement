from django.shortcuts import redirect, render
from django.urls.base import reverse

# Create your views here.
def Profile_admin(request):
    if request.user.is_superuser:
        return render(request, "Admin/admin_dashboard.html")
    else:
        return redirect(reverse('accounts:home')) 