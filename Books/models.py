from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    
class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    
    # I comment it just to save database resources instead of creating a column in the database for slug
    # I prefered to make it as a instance property
    # slug = models.SlugField(max_length = 150, blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.CharField(max_length=150)
    user = models.ManyToManyField(User, through='Borrowing')
    total_number_of_copies = models.IntegerField(default=0)
    available_number_of_copies = models.IntegerField(null=True, blank=True) 
    created_at = models.DateTimeField(null=True, blank=True , default=timezone.now) 

    @property
    def slug(self):
        return slugify(self.title)
    def __str__(self):
        return self.title


class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowing_date = models.DateField(default=timezone.now)
    return_date = models.DateField(default=timezone.now)


