from django.urls import path
from .views import Profile_admin
app_name = 'admin_dashboard'
urlpatterns = [
    path('', Profile_admin, name='profile_admin'),
]