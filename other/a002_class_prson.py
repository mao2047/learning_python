class Person:

    def __init__ (self, name):
        self.name = name

    def talk(self):
        print(f"Hi!, my name is {self.name}")


person1 = Person("Lenin")
person1.talk()

person2 = Person("Stalin")
person2.talk()
