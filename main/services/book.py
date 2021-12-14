import re
from abc import ABC, abstractmethod
from django.core.exceptions import ValidationError
from main.models import Book

class AbstractCreateBookService(ABC):
    # @abstractmethod
    def create_book(self, book: Book) -> Book: pass


class CreateBookService(AbstractCreateBookService):
    book_number_regex = re.compile(r'^[A-Z]{1,2}-[0-9]{2,3}$')

    def create_room(self, book: Book) -> Book:
        book.number = book.number.upper()
        if not self.book_number_regex.match(book.number):
            raise ValidationError('Book number must have one or two letters followed by a dash, then two to three numbers')

        book.save()
        return book
