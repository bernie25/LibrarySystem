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






    
