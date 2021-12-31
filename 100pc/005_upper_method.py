class Person():
    def __init__(self):
        self.name = ""

    def getString(self):
        self.name = input("introduce nombre: ")

    def printString(self):
        print(self.name.upper())


object1 = Person()
object1.getString()
object1.printString()
