from django.shortcuts import render

#Add a book to the library
def homePage(request):
    return render(request, 'homePage.html')
