class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    
    def bark(self):
        print("Bark")

class Cat(Mammal):
    def purr(self):
        print("Purrr")


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.walk()
