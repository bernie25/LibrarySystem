from django.contrib import admin
from .models import Book, Category, LibrarySystem, BookInstance

# class LibrarySystemAdmin(admin.ModelAdmin):
#     list_display = ('title')
"""Minimal registration of Models.
admin.site.register(LibrarySystem)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(BookInstance)
"""
admin.site.register(LibrarySystem)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(BookInstance)

class BooksInstanceInline(admin.TabularInline):
    """Defines format of inline book instance insertion (used in BookAdmin)"""
    model = BookInstance

class BookAdmin(admin.ModelAdmin):
    """Administration object for Book models.
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of book instances in book view (inlines)
    """
    list_display = ('title', 'author', 'category')
    inlines = [BooksInstanceInline]


#@admin.register(BookInstance)
#class BookInstanceAdmin(admin.ModelAdmin):
    #   list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    #  list_filter = ('status', 'due_back')

  #  fieldsets = (
    #   (None, {
     
    #       'fields': ('book', 'imprint', 'id')
     #   }),
      #  ('Availability', {
      #      'fields': ('status', 'due_back', 'borrower')
     #   }),
  #  )