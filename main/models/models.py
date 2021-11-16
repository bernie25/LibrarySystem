#Database layout
from enum import Enum
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class LibrarySystem(models.Model):
    book_name = models.CharField(max_length=200)

    def _str_(self):
        return self.title

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def _str_(self):
        return self.title

class BookingStateEnum(Enum):
    AVAILABLE = 'available'
    UNAVAILABLE = 'unavailable'

class BookingDetails(models.Model):
    book_name = models.CharField(max_length=200)
    student_number = models.IntegerField()

    def book(self): self.booking_state = BookingStateEnum.BOOKED

#https://dev.to/thepylot/create-advanced-user-sign-up-view-in-django-step-by-step-k9m

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)

def __str__(self):
    return self.user.username

#@receiver decorator, we can link a signal with a function
#sender - The model class.
@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
   #instance - The actual instance being saved.
   #created - A boolean; True if a new record was created.
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()  
