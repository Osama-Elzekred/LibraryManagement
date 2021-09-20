from .forms import BookCreateForm, CategoryCreateForm
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Book, Category
from django.views.generic import ListView
from django.urls import reverse

#Book class views 
class BookListView(ListView):
    model = Book
    context_object_name = 'Books'
    ordering = ['-created_at']

class BookCreateView(CreateView):
    model  = Book
    form_class = BookCreateForm
    template_name_suffix = '_create_form'
    def form_valid(self, form):
        return super().form_valid(form)
    
class BookDeleteView(DeleteView):
    model = Book
    context_object_name = 'book'
    success_url = "/"
        
    def get_object (slef):
        slug_ = slef.kwargs.get('slug')
        return get_object_or_404(Category, id=slug_)

class BookUpdateView(UpdateView):
    model = Book
    template_name_suffix = '_update_form'
    context_object_name = 'book'

#Category class views 
class CategoryListView(ListView):
    model = Category
    ordering = ['title']
    context_object_name = 'categories'
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name_suffix = '_create_form'
class CategoryDeleteView(DeleteView):
    model = Category
    context_object_name = 'category'

    def get_success_url(self):
        return reverse('Books:category_list')

    def get_object (slef):
        slug_ = slef.kwargs.get('slug')
        return get_object_or_404(Category, slug=slug_)

