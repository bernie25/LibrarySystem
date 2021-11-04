#Database layout
from abc import ABC, abstractmethod
from . import views
from django.db import models


class LibrarySystem(models.Model):
    book_name = models.CharField(max_length=200)

    def _str_(self):
        return self.title


        #Business logic
        # 
        #Design patterns, Added Value 
        #Factory method - Loan Book - instead of new

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    
    def _str_(self):
        return self.title


# class State(ABC):
#     #Used to make context method as property
#     @property
#     def context(self) -> Context:
#         return self._context

#     #decorator to aother overload of the context method as property 
#     #setter method
#     #_context is protected now
#     @context.setter
#     def context(self, context:Context) -> None:
#         self._context = context
    
#     #one markStatus is called then state of Context changes
#     @abstractmethod
#     def markStatus(self) -> None:
#         pass


# class Context:

#     _state = None

#     def __init__(self, state: State) -> None:
#         self.setState(state)

#     def setState(self, state: State):

#         print(f"Book Status {type(state).__name__}")
#         self._state = state
#         self._state.context = self

#     def markStatus(self):
#         self._state.markStatus()
