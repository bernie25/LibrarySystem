from django.urls import path

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.forms.bookform import FormBook
from main.models import Book
from main.services.book import CreateRoomService
from main.views import views
from main.views.book import BookCreateView
from main.views.booking import bookingView, createBookingView
from main.views.addBook import addBook
from main.views.homepage import homePage
from main.views.signup import signup

urlpatterns = [
    path('', views.home, name="home"),
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

    path('home/', homePage, name='homePage'),
    path('addBook/', addBook, name='addBook'),
    path('booking/', bookingView, name='booking'),
    path('booking/create/', createBookingView, name='createBooking'),

        # path('booking/create/', 
            #     createBookingView.as_view(service_class= AbstractCreateBookingService,
            #     form_class=BookingForm,
            #     model=BookingDetails,
            #     template_name='main/templates/booking.html',
            #     success_url='.'
            #     ), 
            #     name='create/booking'),
]
