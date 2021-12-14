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
from main.services.booking.booking import CreateBookingService
#views
from . import views
from main.views.views import *
from main.views.book import BookCreateView
from main.forms.bookingForm import BookingForm
from main.models import BookingDetails
from main.views.views import libraryView
from main.views.booking import bookingView, createBookingView
from main.views.addBook import addBook
from main.views.homepage import homePage
from main.views.booking import bookingView, createBookingView
from main.views.addBook import addBook
from main.views.homepage import homePage
from main.views.Library import library
from main.views.signup import signup

from main.views.views import *
from main.views import views
from django.contrib.auth import views as auth_views
from main.views.views import logout

urlpatterns = [
    #path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
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
    # path('book_form/', bookform, name='book_form'),
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate,
        #name='activate'),
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
    ##############################################################################
    path('books/', views.BookListView.as_view(), name='books'),
    path('bookdetail/', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
]