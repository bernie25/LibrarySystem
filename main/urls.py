from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('home/', views.User.as_view(), name='home'),
]