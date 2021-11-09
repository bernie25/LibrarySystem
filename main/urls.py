from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homePage, name='homePage'),
    path('addBook/', views.addBook, name='addBook'),
    path('booking/', views.booking, name='booking'),
]