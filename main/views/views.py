from django.http import HttpResponse
from django.shortcuts import render

from main.services.requestBook.bookreq import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from main.models import *
from main.forms import *

#Add a book to the library
def homePage(request):
    return render(request, 'homePage.html')

def index(request):
    return HttpResponse("Hello")

#Add a book to the library
def addBook(request):
    if request.method == 'POST':
        print(type(request.POST))
        print(request.POST.keys())
        print(request.POST)
    context = {
        'title' : "Add Book",
    }
    return render(request, 'addBook.html', context=context)

#Booking
def booking(request):
    return render(request, 'booking.html')


#Return Book

#Report Book

@login_required(login_url='login')
def home(request):
		if(request.GET.get('mybtn')):
			print("Book now available") 
		return render(request, '../templates/requestBook.html')
		# bookAvailableClass()

def reqbook(request):
		return render(request,'../templates/requestBook.html')

def signup(request):
		return render(request,'../templates/signup.html')
        
def logout(request):
		return render(request,'../templates/logout.html')

#Create Library
def libraryView(request, *args, **kwargs):
    
    view_all_library = Book.objects.all()
    return render(request, '../templates/library.html', 
    {'view_all_library': view_all_library})









    
