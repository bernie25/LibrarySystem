# import functools
# from abc import ABC, abstractmethod
# from main.models import BookingDetails 


# class AbstractCreateBookingService(ABC):
#     @abstractmethod
#     def create_booking(self, booking: BookingDetails) -> BookingDetails: pass

# class CreateBookingService(AbstractCreateBookingService):
#     def create_booking(self, booking: BookingDetails) -> BookingDetails:
#         booking.book()
#         booking.save()
#         return booking
