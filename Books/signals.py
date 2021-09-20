from django.db.models.signals import m2m_changed, pre_save 
from django.dispatch import receiver
from .models import Book , Category
from django.template.defaultfilters import slugify
#this signal will be emitted when the an object of model Book is created (not created in database as it pre_save will be sent at the beginning of the save method)
#if the admin did not add the available number of copies it will be by default set to be equal to the total number of copies
@receiver(pre_save, sender=Book)
def addnig_defaut_fields(sender, instance, *args, **kwargs):
    if not instance.available_number_of_copies:
        instance.available_number_of_copies = instance.total_number_of_copies

    # this is in case you want it as a column in the database.
    # note that the admin don't have to enter the slug field so I used signal to make it's default to be equal to slugified title.
    instance.slug = slugify(instance.title)
    

#I did that just to simplify dealing with the book model 

#this signal will be emitted whenever any chages happenned in the m2m relationship 
#which mean any user borrows a copy of the book the number of copies for this book will be reduced by 1
# and when a user return the borrowed copy of the book the number of copies will be increased by 1  
@receiver(m2m_changed, sender=Book.user.through)
def update_available_number_of_copies(*args , **kwargs):
    if kwargs['action'] == 'post_add':
        kwargs['instance'].available_number_of_copies -= 1
    elif kwargs['action'] == 'post_remove':
        kwargs['instance'].available_number_of_copies += 1

@receiver(pre_save, sender=Category)
def addnig_defaut_category_fields(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)