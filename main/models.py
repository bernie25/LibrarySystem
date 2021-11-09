#Database layout
from enum import Enum
from django.db import models

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
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=200)
    student_number = models.IntegerField()

    def book(self): self.booking_state = BookingStateEnum.BOOKED    
    #def __str__(self) -> str: return self.id and self.book_name and self.student_number

