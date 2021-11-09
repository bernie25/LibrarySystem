#State Design Pattern
#Bernie
from main.models import *
from abc import ABC

class BookState(ABC):
    name ='state'
    allowed = []

    def __init__(self, bookState: Book):
        self.bookState = bookState

    def status(self, state):
        # Switch to new state
        if state.name in self.allowed:
            print("Book is Available",self,"new",state.name)
            self.__class__ = state
        else:
            print('Current:',self,' => switching to',state.name,'not possible.')

    # def __str__(self):
    #     return self.name

class Available(BookState):
    name = "available"
    allowed = ['unavailable']

class Unavailable(BookState):
    name = "unavailable"
    allowed = ['available']

class Book(ABC):

    def __init__(self, genre='CompSci'):
        self.genre = genre
        # Default state is available
        self.state = Available()
    
    def change(self, state):
        self.state.switch(state)

if __name__ == "__main__":
    status = Book()
    status.change(Available)
    status.change(Unavailable)