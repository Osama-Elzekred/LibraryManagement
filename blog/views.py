from django.shortcuts import render
from django.views import View
# Create your views here.
class BlogView(View):
    def get (self, request, *args, **kwargs):
        return render(request, 'blog/blog.html', {})
