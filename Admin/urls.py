from django.urls import path
from .views import Profile_admin, add_author
app_name = 'Admin'
urlpatterns = [
    path('', Profile_admin, name='admin_dashboard'),
    path('add_author/', add_author, name='add_author'),
]