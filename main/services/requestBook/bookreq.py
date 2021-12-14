from .observer import abstractSubject
from .observer import abstractObserver

class bookName(abstractSubject):
    __instance = None
    book = 0
    @staticmethod
    def getInstance():
        if bookName.__instance == None:
            bookName()
        return bookName.__instance


class bookAvailableClass(abstractObserver):      

    def __init__(self):
        super().__init__()


    def update(self, bookAvail, obj):
        if bookAvail == 1:
            bookName = bookAvail.getValue("name")
            print("Book" + str(bookName) + "is now available.")

        else:
            pass

