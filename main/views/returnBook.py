from django.shortcuts import render

from main.models import *
from main.forms import *

#Return Book
def returnBookView(request, *args, **kwargs):

    view_all_library = Book.objects.all()
    return render(request, '../templates/returnBook.html', {'view_all_library': view_all_library})
