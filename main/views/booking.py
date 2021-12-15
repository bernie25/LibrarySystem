from typing import Callable
from django.shortcuts import render
from django.db.models import Model

from main.services.booking import *
from main.models import BookingDetails
from main.services.booking.booking import AbstractCreateBookingService
from main.utils import BaseCreateView, auth_required

#Booking
def bookingView(request):
    return render(request, 'booking.html')

class createBookingView(BaseCreateView, AbstractCreateBookingService):
    service_class: Callable[[], AbstractCreateBookingService] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = self.service_class()

    @auth_required()
    def create_booking(self, booking: BookingDetails) -> BookingDetails:
        return super().create_booking(booking)

    def save_model_instance(self) -> Model: return self.create_booking(self.object)
