from .observer import abstractSubject
from .observer import abstractObserver

class bookName(abstractSubject):
    """
        Concrete Subject - Patient in this demo
    """

    def __init__(self, name):
        super().__init__()  
        self.name = name
        self.__physioParams = {"temperature": 0.0, "heartrate": 0.0, "oxygen": 0.0, "respiration": 0.0}

    ## function to the observed subject's state
    def setValue(self, measureType, val):
        if measureType in self.__physioParams:
            self.__physioParams[measureType] = val
            # print("{}'s {} set to: {}".format(self.name, measureType, str(val)) )
            self.notifyObservers()
        else:
            print("Parameter type \"{}\" not yet supported.".format(measureType))

    def getValue(self, measureType):
        if measureType in self.__physioParams:
            return self.__physioParams[measureType]
        else:
            return None



class bookAvailableClass(abstractObserver):      

    def __init__(self):
        super().__init__()


    def update(self, bookAvail, obj):
        if bookAvail == 1:
            bookName = bookAvail.getValue("name")
            print("Book" + str(bookName) + "is now available.")

        else:
            pass

