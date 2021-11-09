from abc import ABC, abstractmethod
from django.http import HttpResponse
from django.shortcuts import render


# https://github.com/SeniorFlacko/FactoryMethod


#Find an existing class that contains state-dependent code,
#  or create a suitable context class. 
# It should include a reference to a specific state as well
#  as a method for switching between states.


# Create a common State interface for all concrete states.
# The State interface specifies all of the methods that all
# Concrete States must implement and a backreference to the 
# Context object. 
# States can change the Context to another state by using
# this backreference.


# class BookAvailable(models.State):
#     #_state = 'Available'

#     def markStatus(self) -> None:
#         print("Book is available")
#         self.context.setState(BookUnavailable())
#         # if status == 'Available':
#         #     self._state = 'Available'
#         # elif status == 'Unavailable':
#         #     self._state = 'Unavailable'

# class BookUnavailable(models.State):
#     def markStatus(self) -> None:
#         print("Book is Unavailable")
#         self.context.setState(BookAvailable())

# app = Context(BookAvailable())
# app.markStatus()
# app.markStatus()

def index(request):
    return HttpResponse("Hello")

#Add a book to the library
def homePage(request):
    return render(request, 'homePage.html')

#Add a book to the library
def addBook(request):
    if request.method == 'POST':
        print(type(request.POST))
        print(request.POST.keys())
        print(request.POST)
    context = {
        'title' : "Add Book",
    }
    return render(request, 'addBook.html', context=context)

#Booking
def booking(request):
    return render(request, 'booking.html')

#Login


#Logout

#Return Book

#Report Book

#ViewLibrary