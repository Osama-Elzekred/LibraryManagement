"""MyLibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Books.views import author_book_list, category_book_list
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import ContactUs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', ContactUs.as_view(), name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('home/', include('Books.urls', namespace='Books')),
    path('dashboard_admin/', include('Admin.urls', namespace='Admin')),
    path('category/<str:slug>', category_book_list, name='category_book_list'),
    path('author/<str:slug>', author_book_list, name='author_book_list'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
