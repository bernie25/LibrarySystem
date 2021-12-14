from django.urls import path
from django.urls import path

#Forms Import
from main.forms.bookform import FormBook
from main.forms.bookingForm import BookingForm

#Models import
from main.models import Book, BookingDetails

#Services import
from main.services.book import CreateBookService
from main.services.booking.booking import CreateBookingService

#Views import
from main.views.views import libraryView
from main.views import views
from main.views.book import BookCreateView
from main.views.booking import bookingView, createBookingView
from main.views.addBook import addBook
from main.views.homepage import homePage
from main.views.signup import signup
from main.forms.bookingForm import BookingForm
from main.models import BookingDetails
from main.services.booking.booking import CreateBookingService
from main.views.booking import bookingView, createBookingView
from main.views.addBook import addBook
from main.views.homepage import homePage

urlpatterns = [
    #path('', views.home, name="home"),
    #path('register/', views.registerPage, name="register"),
	#path('login/', views.loginPage, name="login"),  
	#path('logout/', views.logoutUser, name="logout"),
    path('reqbook/', views.reqbook, name="reqbook"),
    path('signup/', views.signup, name="signup"),
    path('book/new/',
        BookCreateView.as_view(
                            service_class=CreateBookService,
                            form_class=FormBook,
                            model=Book,
                            template_name='../templates/addBook.html', success_url='.'),
                            name='add-book'),

    #Homepage
    path('', homePage, name='homePage'),

    #View Booking
    path('booking/', bookingView, name='booking'),

    path('register/', views.registerPage, name="register"),

	path('login/', views.loginPage, name="login"),  
    
	path('logout/', views.logoutUser, name="logout"),
    #Create a new booking
    path('booking/create/', 
            createBookingView.as_view(service_class= CreateBookingService,
            form_class=BookingForm,
            model=BookingDetails,
            template_name='createBooking.html',
            success_url='.'), 
            name='booking-create'),
            

    path('library/', libraryView),
]
