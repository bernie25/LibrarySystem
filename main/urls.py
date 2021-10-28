from django.urls import path
from . import views

urlpatterns = [
    #path('user/', views.LibrarySystemView, name='user'),
    path('home/', views.index, name='index'),
]