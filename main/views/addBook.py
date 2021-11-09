from django.shortcuts import render

def addBook(request):
    return render(request, 'addBook.html')
