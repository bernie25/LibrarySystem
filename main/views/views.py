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

#Signup basic registration function with email confirmation
def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        # user can't login until link confirmed
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        subject = 'Please Activate Your Account'
        # load a template like get_template() 
        # and calls its render() method immediately.
        message = render_to_string('activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })

        #cleaned_data holding the validated form data and authenticate() method takes credentials as keyword arguments,
        #username and password for the default case, checks them against each authentication backend, and returns a User object if the credentials are valid for a backend.
        user.email_user(subject, message)
        return redirect('activation_sent')
    else:
            form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

#
