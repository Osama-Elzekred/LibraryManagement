from django.urls import path
from .views import BookCreateView, BookListView, BookDeleteView, BookUpdateView, CategoryCreateView, CategoryDeleteView, CategoryListView
app_name = 'Books'
urlpatterns = [
    path('',BookListView.as_view() , name='home'),
    path('book/delete/<int:id>', BookDeleteView.as_view(), name='book_delete'),
    path('book/update/<int:id>', BookUpdateView.as_view(), name='book_update'),
    path('book/create', BookCreateView.as_view(), name='book_create'),
    path('category/create', CategoryCreateView.as_view(), name='category_create'),
    path('category/delete/<int:id>', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/list', CategoryListView.as_view(), name='category_list'),
]