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
#imports
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from datetime import datetime,timedelta

#UserExtend() model extends the user model as the user model contains only email, first name, last name and password. 
class UserExtend(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.IntegerField()
    def __str__(self):
       return self.user.username

#The AddBook() model stores the data of books that are added in the library
class AddBook(models.Model):
    user = models.ForeignKey(User,default = 1, on_delete=models.CASCADE)
    bookid=CharField(max_length=10)
    bookname=CharField(max_length=50)
    subject=CharField(max_length=20)
    category= models.CharField(max_length = 10)
    def __str__(self):
        return str(self.bookname)+"["+str(self.bookid)+']'

#def expiry()
def expiry():
    return datetime.today() + timedelta(days=15)

#Issue Book model
class IssueBook(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    studentid=CharField(max_length=20)
    book1=models.CharField(max_length=20)
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=expiry)
    def __str__(self):
        return self.studentid

#redirects the user to the page where the book can be returned by entering the bookid
class ReturnBook(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bookid2=models.CharField(max_length=20)

#
class AddStudent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    sname=models.CharField(max_length=30)
    studentid=models.CharField(max_length=20)
    def __str__(self):
        return self.sname+'['+str(self.studentid)+']'
