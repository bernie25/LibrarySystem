from django.contrib.auth.models import AbstractUser
from django.db import models
from enum import Enum

class User(AbstractUser):
    pass

class Studentmanager(models.Manager):
    def create_student(self, user, id_no, telephone):
        id=user.id
        newuser=self.model(user_id=id, phone=telephone, id_no=id_no)
        newuser.save(using=self._db)
        return newuser

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=17, blank=True)
    credit_card = models.CharField(max_length=19)
    objects=Studentmanager()


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


class Librarianmanager(models.Manager):
    def create_librarian(self, user):
        id=user.id
        newuser=self.model(user_id=id)
        newuser.save(using=self._db)
        return newuser

class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    objects=Librarianmanager()

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    bookname = models.CharField(max_length=30, blank=True)
    bookcode = models.CharField(max_length=30, blank=True)
    category = models.CharField(max_length=30, blank=True)

    def __str__(self) -> str: return self.bookname and self.category and self.bookcode
