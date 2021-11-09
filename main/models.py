#Database layout

from django.db import models

class LibrarySystem(models.Model):
    book_name = models.CharField(max_length=200)

    def _str_(self):
        return self.title


        #Business logic
        # 
        #Design patterns, Added Value 
        #Factory method - Loan Book - instead of new

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    
    def _str_(self):
        return self.title
