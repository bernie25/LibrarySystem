#Django Imports 
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

#Services Import 
from main.services.requestBook.bookreq import *

#Views Import
from main.views.book import Book

#Models import
from main.models import *
from main.models import Author


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

#Make Booking
def booking(request):
    return render(request, 'booking.html')

#Login
@login_required(login_url='login')
def home(request):
		if(request.GET.get('mybtn')):
			print("Book now available") 
		return render(request, '../templates/requestBook.html')
		# bookAvailableClass()

#Signup
def signup(request):
		return render(request,'../templates/signup.html')

#Logout
def logout(request):
		return render(request,'../templates/logout.html')

#View Library
def libraryView(request, *args, **kwargs):
    
    view_all_library = Book.objects.all()
    return render(request, '../templates/library.html', 
    {'view_all_library': view_all_library})

#Register
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = UserCreationForm()
		if request.method == 'POST':
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + username)

				return redirect('login')

		return render(request, '../templates/register.html', {'form':form})

#Login
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, '../templates/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

#Signup basic registration function using factory design pattern
from main.views.Factorysignup import SignUpForm
from main.views.userfactory import UserFactory
def signup(request):
    if request.method == 'POST':
        factory = UserFactory()
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            factory.createuser(form, new_user)
            new_user.save()
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


