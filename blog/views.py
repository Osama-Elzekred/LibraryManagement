from django.shortcuts import render
from django.views import View
from Books.models import Category
# Create your views here.
class BlogView(View):
    def get (self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'blog/blog.html', {'Categories': categories})
