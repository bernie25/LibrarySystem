from django.contrib.auth.models import AbstractUser
from django.db import models
from enum import Enum
import re
from django import forms


class User(AbstractUser):
    pass

class Studentmanager(models.Manager):
    def create_student(self, user, id_no):
        id=user.id
        newuser=self.model(user_id=id, id_no=id_no)
        newuser.save(using=self._db)
        return newuser

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    id_no = models.IntegerField(max_length=8)
    objects=Studentmanager()

class Librarianmanager(models.Manager):
    def create_librarian(self, user):
        id=user.id
        newuser=self.model(user_id=id)
        newuser.save(using=self._db)
        return newuser

class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    objects=Librarianmanager()



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
    bookname = models.CharField(max_length=30, blank=True)
    bookcode = models.IntegerField()
    booking_state = models.CharField(max_length=20, choices=BookingStateEnum.tuples(), default=BookingStateEnum.PENDING)
    category = models.CharField(Category, default=0, max_length=20)

    # # def __str__(self) -> str: return self.bookname and self.category and self.bookcode
    # def __str__(self):
    #     return self.bookname

    def book(self): self.booking_state = BookingStateEnum.AVAILABLE
    def __str__(self) -> str: return self.bookname

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
