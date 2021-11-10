from typing import Callable

from django.db.models import Model

from main.models.book import Book
from main.services.book import AbstractCreateRoomService
from main.views.utils import BaseCreateView, auth_required


class BookCreateView(BaseCreateView, AbstractCreateRoomService):
    service_class: Callable[[], AbstractCreateRoomService] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = self.service_class()

    @auth_required()
    def create_book(self, instance: Book) -> Book:
        return self.service.create_book(instance)

    def save_model_instance(self) -> Model:
        return self.create_book(self.object)