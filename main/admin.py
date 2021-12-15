from django.contrib import admin
from .models import Book, Category, LibrarySystem

admin.site.register(LibrarySystem)
admin.site.register(Book)
admin.site.register(Category)
