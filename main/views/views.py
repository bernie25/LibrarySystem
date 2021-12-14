from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import Student, User
from main.services.requestBook.bookreq import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from main.views.book import Book
from datetime import date
from main.forms import bookform

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render
from main.models import *
from django.shortcuts import render
from main.forms.signupform import SignUpForm
from main.views.userfactory import UserFactory
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import login_required, permission_required

# from .forms import RenewBookForm
from main.forms.renewbookform import RenewBookForm

from django.urls import reverse_lazy
from main.models import Author
from django.views.generic.edit import DeleteView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin


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
