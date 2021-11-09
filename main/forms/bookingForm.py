from django import forms

from main.models import BookingDetails

class BookingForm(forms.ModelForm):
    class Meta: 
        model = BookingDetails
        fields = ('book_name', 
                  'student_number',)