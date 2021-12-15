from django import forms

from main.models import Book, BookingStateEnum, CreateBooking

#Form being used for booking Request 

class BookingForm(forms.ModelForm):
    class Meta: 
        model = CreateBooking
        fields = ('bookname',
                  'booking_state',
                  'student_number',)

