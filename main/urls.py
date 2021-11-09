from django.urls import path
from main.views.booking import bookingView, createBookingView
from main.views.addBook import addBook
from main.views.homepage import homePage

urlpatterns = [
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
