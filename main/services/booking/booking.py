import functools
from abc import ABC, abstractmethod
from main.models import Book

class AbstractCreateBookingService(ABC):
    @abstractmethod
    def create_booking(self, booking: Book) -> Book: pass

class CreateBookingService(AbstractCreateBookingService):
    def create_booking(self, booking: Book) -> Book:
        booking.book()
        booking.save()
        return booking
