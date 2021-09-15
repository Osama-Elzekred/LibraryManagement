from django.urls import path
from .views import sign_up , profile
app_name = "accounts"
urlpatterns = [
    path('signup/' , sign_up , name="signup"),
    path('profile/', profile, name="profile")
]
