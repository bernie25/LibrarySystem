#Django Imports 
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#Services Import 
from main.services.requestBook.bookreq import *

#Views Import
from main.views.book import Book

#Models import
from main.models import *
from main.models import Author

#Homepage
def homePage(request):
    return render(request, 'homePage.html')

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
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, '../templates/register.html', context)

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
