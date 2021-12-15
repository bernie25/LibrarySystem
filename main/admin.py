from django.contrib import admin
from .models import Book, Category, CreateBooking, LibrarySystem

# class LibrarySystemAdmin(admin.ModelAdmin):
#     list_display = ('title')

admin.site.register(LibrarySystem)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(CreateBooking)