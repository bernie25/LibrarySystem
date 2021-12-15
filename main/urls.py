from django.urls import path

#Forms Import
from main.forms.bookform import FormBook
from main.forms.bookingForm import BookingForm

#Models import
from main.models import Book, CreateBooking

#Services import
from main.services.book import CreateRoomService
from main.services.booking.booking import CreateBookingService

#Views import
from main.views.views import libraryView
from main.views import views
from main.views.book import BookCreateView
from main.views.booking import bookingView, createBookingView
from main.views.addBook import addBook
from main.views.homepage import homePage
from main.views.signup import signup
from main.views.returnBook import returnBookView


urlpatterns = [
    #path('register/', views.registerPage, name="register"),
	#path('login/', views.loginPage, name="login"),  
	#path('logout/', views.logoutUser, name="logout"),
    path('reqbook/', views.reqbook, name="reqbook"),
    path('signup/', views.signup, name="signup"),
    path('book/new/',
        BookCreateView.as_view(
                            service_class=CreateRoomService,
                            form_class=FormBook,
                            model=Book,
                            template_name='../templates/addBook.html', success_url='.'),
                            name='add-book'),

    #Homepage
    path('homepage/', homePage, name='homePage'),

    #Add a new book
    path('addBook/', addBook, name='addBook'),
    
    #View Booking
    path('booking/', bookingView, name='booking'),

    #Create a new booking
    path('booking/create/', 
            createBookingView.as_view(service_class= CreateBookingService,
            form_class=BookingForm,
            model=CreateBooking,
            template_name='createBooking.html',
            success_url='.'), 
            name='booking-create'),

    #View Library
    path('library/', libraryView),

    #Return Book
    path('return/', returnBookView),
]
