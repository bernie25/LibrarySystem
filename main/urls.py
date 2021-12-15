#django imports
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

#forms
from main.forms.bookform import FormBook
from main.forms.bookingForm import BookingForm

#Models import
from main.models import Book, BookingDetails

#Services import
from main.services.book import CreateBookService
from main.services.booking.booking import CreateBookingService

#Views import 
from . import views
from main.views.views import *
from main.views import views
from main.views.book import BookCreateView
from main.views.booking import bookingView, createBookingView
from main.views.addBook import addBook
from main.views.homepage import homePage
from main.views.Factorysignup import signup
from main.views.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name="home"),
    path('book/new/',
        BookCreateView.as_view(
                            service_class=CreateBookService,
                            form_class=FormBook,
                            model=Book,
                            template_name='../templates/addBook.html', success_url='.'),
                            name='add-book'),
    #Create Booking
    path('booking/create/', 
        createBookingView.as_view(
                            service_class= CreateBookingService,
                            form_class=BookingForm,
                            model=BookingDetails,
                            template_name='createBooking.html',
                            success_url='.'), 
                            name='booking-create'),
  
    #Homepage
    path('', homePage, name='homePage'),

    #View Booking
    path('booking/', bookingView, name='booking'),

    path('register/', views.registerPage, name="register"),

	path('login/', views.loginPage, name="login"),  
    
	path('logout/', views.logoutUser, name="logout"),

    path('signup/', signup, name='signup'),
    path('register/', registerPage, name='register'),
    #path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),

]

