from django.urls import path
from . import views

urlpatterns = [
    #path('user/', views.LibrarySystemView, name='user'),
    path('home/', views.index, name='index'),
    path('addBook/', views.addBook, name='addBook'),

    path('', views.home, name="home"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
]