class abstractSubject():
    """
        Abstract Subject - Abstract patient in this demo
    """

    def __init__(self):
        self.__observers = []

    def addObs(self, observer):
        self.__observers.append(observer)

    def removeObs(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, arg=0):
        for o in self.__observers:
            o.update(self, arg)


class abstractObserver():
    """
        Abstract Observer - Abstract medical device in this demo
    """

    def __init__(self):
        pass

    def update(self):  ## shall be overridden 
        pass