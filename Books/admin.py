from django.contrib import admin
from .models import Book , Borrowing , Category
# Register your models here.
 
admin.site.register(Book)
admin.site.register(Borrowing)
admin.site.register(Category)


 