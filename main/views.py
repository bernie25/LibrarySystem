from django.http import HttpResponse
from django.shortcuts import render

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

#Login
# This is the change 
#Logout

#Return Book

#Report Book

#ViewLibrary