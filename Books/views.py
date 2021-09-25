from django.contrib import messages
from .forms import BookCreateForm, CategoryCreateForm, BookUpdateForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Author, Book, Category
from django.views.generic import ListView
from django.urls import reverse

#Book class views 
class BookListView(ListView):
    model = Book
    template_name = 'Books/book_list.html'
    context_object_name = 'Books'
    ordering = ['-created_at']
    
    def get_context_data(self , **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['Categories'] = Category.objects.all()
        return context

class BookUpdateListView(BookListView):
    template_name = 'Books/book_update_list.html'
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'Books/book_update_form.html'
    context_object_name = 'form'
    form_class = BookUpdateForm
    def post(self, request, *args, **kwargs):
        book_form = BookUpdateForm(request.POST, request.FILES, instance=self.get_object())
        if book_form.is_valid():
            book_form.save()
            messages.success(request, f'{self.get_object().title} Book has been updated successfully!')
        else:
            messages.error(request, 'Invalid Data please try again!')
        return redirect(reverse('Admin:book_update_list'))

class CategoryBooksUpdateView(BookUpdateListView):
    template_name = 'Books/category_update_book.html'
    def get_context_data(self, **kwargs):
        context = super(CategoryBooksUpdateView, self).get_context_data(**kwargs)
        category = Category.objects.filter(slug= self.kwargs['slug']).first()
        context['Books'] = Book.objects.filter(category=category)
        return context

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


#function based views 
def update_list_view(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    context = {'Books': books, 'Categories':categories}
    return render(request, 'Books/book_update_list.html',context)

def category_book_list(request, slug):
    category = Category.objects.filter(slug=slug).first()
    books = category.category_books.all()
    category = Category.objects.all()
    context = {'Books':books, 'Categories':category}
    return render(request, 'Books/category_books.html', context)

def author_book_list(request, slug):
    author = get_object_or_404(Author , slug=slug)
    books = author.author_books.all()
    categories = Category.objects.all()
    context = {'Books':books, 'Author':author, 'Categories':categories}
    return render(request,'Books/author_books.html', context)

def return_book(request, slug):  
    book = Book.objects.filter(slug=slug).first()
    user = request.user
    book.user.remove(user)
    return redirect(reverse('Books:home'))

def borrow_book(request, slug):
    if request.method == 'POST':
        book = Book.objects.filter(slug=slug).first()
        user = request.user
        return_date = request.POST.get('return_date')
        book.user.add(user, through_defaults={'return_date':f'{return_date}'})
        return redirect(reverse('Books:home'))
    else:
        return render(request, "Books/borrow.html")



