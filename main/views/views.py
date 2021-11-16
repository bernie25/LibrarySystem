from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect 
from django.forms import inlineformset_factory
from main.services.requestBook.bookreq import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
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

#Signup basic registration function
def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        #cleaned_data holding the validated form data and authenticate() method takes credentials as keyword arguments,
        #username and password for the default case, checks them against each authentication backend, and returns a User object if the credentials are valid for a backend.
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        #Once user is verified, login() method takes an HttpRequest object and a User object and saves the user’s 
        #ID in the session, using Django’s session framework. Finally, redirect() method is basically redirecting the logged in user to home URL.
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html', {'form': form})