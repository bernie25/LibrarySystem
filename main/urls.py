from django.urls import path
from . import views

urlpatterns = [
    #path('user/', views.LibrarySystemView, name='user'),
    path('home/', views.index, name='index'),
    path('addBook/', views.addBook, name='addBook'),
    path('booking/', views.booking, name='booking'),
]