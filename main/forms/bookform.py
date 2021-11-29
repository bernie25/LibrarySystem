from django import forms

from main.models import Book

class FormBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('bookname',
                  'category',
                  'bookcode',)
