from django.urls import path

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.forms.bookform import FormBook
from main.models.book import Book
from main.services.book import CreateRoomService
from main.views import views
from main.views.book import BookCreateView

urlpatterns = [
    path('home/', views.homePage, name='homePage'),
    path('addBook/', views.addBook, name='addBook'),
    path('booking/', views.booking, name='booking'),

    path('', views.home, name="home"),
    #path('register/', views.registerPage, name="register"),
	#path('login/', views.loginPage, name="login"),  
	#path('logout/', views.logoutUser, name="logout"),
    path('reqbook/', views.reqbook, name="reqbook"),

    path('book/new/',
        BookCreateView.as_view(
                            service_class=CreateRoomService,
                            form_class=FormBook,
                            model=Book,
                            template_name='../templates/addBook.html', success_url='.'),
                            name='add-book'),

]