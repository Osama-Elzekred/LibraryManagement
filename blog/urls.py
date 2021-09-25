from blog.views import BlogView
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', BlogView.as_view() ,name='blog')
]