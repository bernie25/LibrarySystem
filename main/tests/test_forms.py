from django.test import TestCase

from main.forms import bookingForm

class bookingFormTest(TestCase):

    def create_booking_test(self):
        form = bookingForm
        self.assertTrue(form.field['bookname'].label is None)
        self.assertTrue(form.field['booking_state'].label is None)
        self.assertTrue(form.field['student_number'].label is None)

    def create_booking_valid(self):
        data = {
            'bookname': 'TestBook', 
            'booking_state': 'AVAILABLE',
            'student_number': '123'
        }
        form = bookingForm(data)
        self.assertTrue(form.is_valid())
        print("Method: create_booking_valid.")

        u = form.save()
        self.assertTrue(getattr(u, 'bookname'), 'TestBook')
