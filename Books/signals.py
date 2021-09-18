from django.db.models.signals import post_save, pre_save 
from django.dispatch import receiver
from .models import Book 

@receiver(pre_save, sender=Book)
def default_available_number_of_copies(sender, instance, **kwargs):
    if not instance.available_number_of_copies:
        instance.available_number_of_copies = instance.total_number_of_copies
@receiver(post_save, sender=Book)
def available_number_of_copies(sender, instance, **kwargs):
    if instance.available_number_of_copies != 0 :
        instance.available_number_of_copies = instance.total_number_of_copies - len(instance.user.all())
        instance.book.save()

