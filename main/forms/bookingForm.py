from django import forms

from main.models import CreateBooking


class BookingForm(forms.ModelForm):
    class Meta: 
        model = CreateBooking
        fields = ('bookname', 
                  'booking_state',
                  'student_number',)