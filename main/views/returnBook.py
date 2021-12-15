from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from main.forms.bookingForm import BookingForm

from main.models import *
from main.forms import *

#Return Book
def returnBookView(request, *args, **kwargs):
    
    view_all_library = Book.objects.all()
    return render(request, '../templates/returnBook.html', {'view_all_library': view_all_library})


