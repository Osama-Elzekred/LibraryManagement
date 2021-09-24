from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField
    image = models.ImageField(upload_to='Blog_images')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

class CommentReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField    
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)