from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.CharField(max_length=150)
    user = models.ManyToManyField(User, through='Borrowing')
    total_number_of_copies = models.IntegerField(default=0)
    available_number_of_copies = models.IntegerField(null=True, blank=True)    


class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowing_date = models.DateField(default=timezone.now)
    return_date = models.DateField(default=timezone.now)

