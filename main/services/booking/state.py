#State Design Pattern
#Bernie
from main.models import *
from abc import ABC

class BookState(ABC):
    name ='state'
    allowed = []

    def __init__(self, bookState: Book):
        self.bookState = bookState

    def book(self): raise ValueError('Invalid operation in ' + self.__class__.__name__)

    # def status(self, state):
    #     # Switch to new state
    #     if state.name in self.allowed:
    #         print("Book is Available",self,"new",state.name)
    #         self.__class__ = state
    #     else:
    #         print('Current:',self,' => switching to',state.name,'not possible.')

    # def __str__(self):
    #     return self.name

# class BookingContextDecorator(BookingDecorator):
#     def __init__(self, booking: Book):
#         super().__init__(booking)
#         if self.booking_state == str(BookingStateEnum.BOOKED):
#             self.current_state = BookingBookedState(booking)
#         else:
#             self.current_state = BookingPendingState(booking)

#     class Meta:
#         abstract = True

#     def book(self):
#         """
#         pre: self.booking->exists() and self.booking.booking_state = PENDING and self.booking.check_in_date >= today
#                 and self.booking.check_out_date > self.booking.check_in_date
#                 and self.booking.number_of_guests > self.booking.room.room_type.capacity
#                 and (self.booking.discount.start_date <= today and self.booking.discount.end_date >= today)
#                 and Booking -> select(room = self.booking.room,
#                                       check_in_date <= self.booking.check_out_date,
#                                       check_out_date < self.booking.check_int_date) -> isEmpty
#         post: self.booking.booking_state = BOOKED and Payment -> select(booking = self.booking) -> size = 1
#         """
#         self.current_state.book()
#         self.current_state = BookingBookedState(self)
#         self.booking.book()
        
# class Available(BookState):
#     name = "available"
#     allowed = ['unavailable']

# class Unavailable(BookState):
#     name = "unavailable"
#     allowed = ['available']

# class Book(ABC):

#     def __init__(self, genre='CompSci'):
#         self.genre = genre
#         # Default state is available
#         self.state = Available()
    
#     def change(self, state):
#         self.state.switch(state)

# if __name__ == "__main__":
#     status = Book()
#     status.change(Available)
#     status.change(Unavailable)