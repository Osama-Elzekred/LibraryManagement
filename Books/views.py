from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Book, Category
from django.views.generic import ListView

#Book class views 
class BookListView(ListView):
    model = Book
    context_object_name = 'Books'
    ordering = ['created_at']

class BookCreateView(CreateView):
    model  = Book
    

class BookDeleteView(DeleteView):
    model = Book
    

class BookUpdateView(UpdateView):
    model = Book


#Category class views 
class CategoryListView(ListView):
    model = Category
    ordering = ['title']
class CategoryCreateView(CreateView):
    model = Category

class CategoryDeleteView(DeleteView):
    model = Category

