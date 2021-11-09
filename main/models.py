from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from datetime import datetime,timedelta
#Models.py file does the database connectivity.

#UserExtend() model extends the user model
# as the user model contains only email, first name, last name and password. As we also want to save the phone number of a person in the database, 
# we create this model.
class UserExtend(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.IntegerField()
    def __str__(self):
       return self.user.username

#The AddBook() model stores the data of books that are added in the library.
class AddBook(models.Model):
    user = models.ForeignKey(User,default = 1, on_delete=models.CASCADE)
    bookid=CharField(max_length=10)
    bookname=CharField(max_length=50)
    subject=CharField(max_length=20)
    category= models.CharField(max_length = 10)
    def __str__(self):
        return str(self.bookname)+"["+str(self.bookid)+']'
def expiry():
    return datetime.today() + timedelta(days=15)

# IssueBook() model stores the information of the book that is issued and the studentid of the student to who has it.
class IssueBook(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    studentid=CharField(max_length=20)
    book1=models.CharField(max_length=20)
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=expiry)
    def __str__(self):
        return self.studentid

#ReturnBook() model contains the data of the book that is returned.
class ReturnBook(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bookid2=models.CharField(max_length=20)

#AddStudent() model stores the details of the student in the libarary system
class AddStudent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #CharFireld() stores strings in the database.
    sname=models.CharField(max_length=30)
    studentid=models.CharField(max_length=20)
    def __str__(self):
        return self.sname+'['+str(self.studentid)+']'