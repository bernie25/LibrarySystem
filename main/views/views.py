from django.http import HttpResponse
from django.shortcuts import render, redirect 
from django.forms import inlineformset_factory
from main.services.requestBook.bookreq import *

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from main.models import *
from main.forms import *


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

#Return Book

#Report Book

#ViewLibrary

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


@login_required(login_url='login')
def home(request):
		if(request.GET.get('mybtn')):
			print("Book now available") 
		return render(request, '../templates/requestBook.html')
		# bookAvailableClass()

def reqbook(request):

		
		return render(request,'../templates/requestBook.html')