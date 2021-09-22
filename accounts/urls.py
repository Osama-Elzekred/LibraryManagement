from django.urls import path
from .views import UpdateData, sign_up
app_name = "accounts"
urlpatterns = [
    # path('signup/' , SignUp.as_view() , name="signup"),  #I don't know why this way dos't work i will try to do that later on my own
    path('signup/' , sign_up , name="signup"),
    path('profile/', UpdateData.as_view(), name="profile"),
]
