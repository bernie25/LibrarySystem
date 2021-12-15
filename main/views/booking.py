from typing import Callable
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Model, When, Q

from main.services.booking import *
from main.models import BookingDetails, Book, BookingStateEnum
from main.services.booking.booking import AbstractCreateBookingService
from main.utils import BaseCreateView, auth_required
from main.forms.bookingForm import BookingForm 

#Booking
def bookingView(request):
    return render(request, 'booking.html')

def createBooking(request, *args, **kwargs):
    submitted = False
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/booking/create/?submitted=True')
    else:
        form = BookingForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'createBooking.html', {'form': form, 'submitted':submitted})

class createBookingView(BaseCreateView, AbstractCreateBookingService):
    service_class: Callable[[], AbstractCreateBookingService] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = self.service_class()

    @auth_required()
    def create_booking(self, booking: Book) -> Book:
        return super().create_booking(booking)

    def save_model_instance(self) -> Model: return self.create_booking(self.object)
