#django imports
from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
#forms
from main.forms.bookform import FormBook
from main.forms.bookingForm import BookingForm
#models
from main.models import Book
from main.models import BookingDetails
#services
from main.services.book import CreateRoomService
#views
from main.views import views
from main.views.book import BookCreateView
from main.forms.bookingForm import BookingForm
from main.models import BookingDetails
from main.views.views import libraryView
from main.services.booking.booking import CreateBookingService
from main.views.booking import bookingView, createBookingView
from main.views.addBook import addBook
from main.views.homepage import homePage
from main.views.booking import bookingView, createBookingView
from main.views.addBook import addBook
from main.views.homepage import homePage
from main.views.library import library


from main.views.signup import signup
from django.contrib.auth import views as auth_views
from main.views.views import logout
from .views import *

urlpatterns = [
    #path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('reqbook/', views.reqbook, name="reqbook"),
    path('book/new/',
        BookCreateView.as_view(
                            service_class=CreateRoomService,
                            form_class=FormBook,
                            model=Book,
                            template_name='../templates/addBook.html', success_url='.'),
                            name='add-book'),
     path('booking/create/', 
        createBookingView.as_view(
                            service_class= CreateBookingService,
                            form_class=BookingForm,
                            model=BookingDetails,
                            template_name='createBooking.html',
                            success_url='.'), 
                            name='booking-create'),

    path('library/', libraryView),
    path('home/', homePage, name='homePage'),
    path('addBook/', addBook, name='addBook'),
    path('booking/', bookingView, name='booking'),
    path('booking/create/', createBookingView, name='createBooking'),
    path('library', library, name='library'),
    path('signup/', signup, name='signup'),
     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout, name='logout'),
        # path('booking/create/', 
            #     createBookingView.as_view(service_class= AbstractCreateBookingService,
            #     form_class=BookingForm,
            #     model=BookingDetails,
            #     template_name='main/templates/booking.html',
            #     success_url='.'
            #     ), 
            #     name='create/booking'),
]
