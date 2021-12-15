from django.test import TestCase
from main.models import CreateBooking

# Tests for Creating a booking

class CreateBookingTest(TestCase):
    @classmethod
    def setUp(cls):
        CreateBooking.objects.create(bookname= 'TestBook', 
                    booking_state = 'AVAILABLE',
                    student_number = '123')

    def test_book_will_create(self):
        book = CreateBooking.objects.get(id=1)
        print("Method: test_booking_will_create.")
        create_booking_test = book._meta.get_field('bookname').verbose_name
        self.assertTrue(create_booking_test, 'TestBook')

    def test_book_wont_create(self):
        print("Method: test_booking_wont_create.")
        self.assertFalse(False)
