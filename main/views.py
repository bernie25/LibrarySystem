from django.http import HttpResponse
from django.shortcuts import render

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


#Return Book

#Report Book

#ViewLibrary