from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homePage, name='homePage'),
    path('addBook/', views.addBook, name='addBook'),
]