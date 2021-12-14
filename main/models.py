from django.contrib.auth.models import AbstractUser
from django.db import models
from enum import Enum
import re
from django import forms
from datetime import datetime,timedelta
from django.urls import reverse  # To generate URLS by reversing URL patterns

class User(AbstractUser):
    pass

class Studentmanager(models.Manager):

    def create_student(self, user, student_number):
        id=user.id
        newuser=self.model(user_id=id, student_number=student_number)
        newuser.save(using=self._db)
        return newuser

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student_number = models.IntegerField(max_length=8)
    objects=Studentmanager()
    def __str__(self):
        return str(self.user) + "["+str(self.student_number)+']'

class Librarianmanager(models.Manager):

    def create_librarian(self, user):
        id=user.id
        newuser=self.model(user_id=id)
        newuser.save(using=self._db)
        return newuser

class Librarian(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    objects=Librarianmanager()

###########################################################################################
class LibrarySystem(models.Model):

    book_name = models.CharField(max_length=200)

    def _str_(self):
        return self.title

class BookingStateEnum(Enum):

    PENDING = 'pending'
    AVAILABLE = 'available'
    UNAVAILABLE = 'unavailable'

    @classmethod

    def tuples(cls): return tuple((state.name, state.value) for state in cls)

class Category(models.Model):

    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Book(models.Model):

    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    bookname = models.CharField(max_length=30, blank=True)
    bookcode = models.IntegerField()
    booking_state = models.CharField(max_length=20, choices=BookingStateEnum.tuples(), default=BookingStateEnum.PENDING)
    category = models.CharField(Category, default=0, max_length=20)

    # # def __str__(self) -> str: return self.bookname and self.category and self.bookcode
    # def __str__(self):
    #     return self.bookname
    class Meta:
        ordering = ['bookname', 'author']

    def book(self): self.booking_state = BookingStateEnum.AVAILABLE


    def __str__(self) -> str: return self.bookname and self.category and self.bookcode


class BookingDetails(models.Model):

    book_name = models.CharField(max_length=200)
    student_number = models.IntegerField()

    def book(self): self.booking_state = BookingStateEnum.BOOKED

class BookCreate(models.Model):

    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=200)
    student_number = models.IntegerField()

    def book(self): self.booking_state = BookingStateEnum.BOOKED    
    #def __str__(self) -> str: return self.id and self.book_name and self.student_number

import uuid  # Required for unique book instances
from datetime import date

#https://stackoverflow.com/questions/70009695/django-contrib-admin-sites-alreadyregistered-the-model-bookinstance-is-already
class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='d',
        help_text='Book availability')

class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.id, self.book.title)

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)
###################################################################################
#sign up fields
class Username(forms.CharField):

    def clean(self, value):
        value = value.replace(' ', '')
        if (len(value) > 26):
            raise forms.ValidationError(self.error_messages['Username should be less than 26 characters'])
        ''''
        elif (User.objects.get(value=uname) is not None):
            raise forms.ValidationError(self.error_messages['Password should be more than 6 characters'])
        '''''
        return value    

class Password(forms.CharField):

    def clean(self, value):
        value = value.replace(' ', '')
        if (len(value) < 6 or len(value) > 8):
            raise forms.ValidationError(self.error_messages['Password must be at least 6 characters'])
        return value

class Name(forms.CharField):

    def clean(self, value):
        value = value.replace(' ', '').replace('-', '').replace('\'', '')
        if (len(value) > 53):
            raise forms.ValidationError(self.error_messages['Name must be less than 52 characters long'])
        elif (re.search(r"[1-9]", value) is not None):
            raise forms.ValidationError(self.error_messages['Name must be less than 52 characters long'])
        return value


class id_no(forms.CharField):

    def clean(self, value):
        value = value.replace(' ', '').replace('-', '')
        if (len(value) > 8):
            raise forms.ValidationError(self.error_messages['ID numberis only 8 numbers'])
        elif (re.search("[a-zA-Z0-9\W]") is not None):
            raise forms.ValidationError(self.error_messages['Only numbers allowed'])
        return value
