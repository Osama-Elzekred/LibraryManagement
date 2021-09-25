from django.urls import path
from .views import Profile_admin, add_author
from Books.views import CategoryBooksUpdateView, BookCreateView, BookDeleteView, BookUpdateView, BookUpdateListView, CategoryCreateView, CategoryDeleteView, CategoryListView
app_name = 'Admin'
urlpatterns = [
    path('', Profile_admin, name='admin_dashboard'),
    path('add_author/', add_author, name='add_author'),
    path('category/<str:slug>', CategoryBooksUpdateView.as_view() , name='update_category_books'),
    path('book/delete/<str:slug>', BookDeleteView.as_view(), name='book_delete'),
    path('book/update/<str:slug>', BookUpdateView.as_view(), name='book_update'),
    path('book/update/', BookUpdateListView.as_view(), name='book_update_list'),
    path('book/add/', BookCreateView.as_view(), name='add_book'),
    path('category/add/', CategoryCreateView.as_view(), name='add_category'),
    path('category/delete/<str:slug>', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/list/', CategoryListView.as_view(), name='list_categories'),
]