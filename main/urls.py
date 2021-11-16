from django.urls import path

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.forms.bookform import FormBook
from main.models.book import Book
from main.services.book import CreateRoomService
from main.views import views
from main.views.book import BookCreateView
from main.views.booking import bookingView, createBookingView
from main.views.addBook import addBook
from main.views.homepage import homePage
from django.conf.urls import url
from main.views import signup, activation_sent, activate

urlpatterns = [
    path('', views.homePage, name="home"),
    #path('register/', views.registerPage, name="register"),
	#path('login/', views.loginPage, name="login"),  
	#path('logout/', views.logoutUser, name="logout"),
    path('reqbook/', views.reqbook, name="reqbook"),

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
    

    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('sent/', activation_sent, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
        # path('booking/create/', 
            #     createBookingView.as_view(service_class= AbstractCreateBookingService,
            #     form_class=BookingForm,
            #     model=BookingDetails,
            #     template_name='main/templates/booking.html',
            #     success_url='.'
            #     ), 
            #     name='create/booking'),
]
