from django.urls import path
from .views import BookListView, return_book, borrow_book
app_name = 'Books'
urlpatterns = [
    path('',BookListView.as_view() , name='home'),
    path('return/<str:slug>', return_book, name='return'),
    path('borrow/<str:slug>', borrow_book, name='borrow'),

]
