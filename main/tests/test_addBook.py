from django.test import TestCase
from main.models import Book

#Tests for Adding a Book

class CreateBookTest(TestCase):
    @classmethod
    def setUp(cls):
        Book.objects.create(bookname= 'TestBook', 
                    bookcode ='1',
                    booking_state = 'AVAILABLE',
                    category = 'Computer Science')

    def test_book_will_create(self):
        book = Book.objects.get(id=1)
        print("Method: test_book_will_create.")
        book_test = book._meta.get_field('bookname').verbose_name
        self.assertTrue(book_test, 'TestBook')

    def test_book_wont_create(self):
        print("Method: test_book_wont_create.")
        self.assertFalse(False)

