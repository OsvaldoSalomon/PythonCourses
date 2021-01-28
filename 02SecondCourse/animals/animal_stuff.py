class Animal:
    def __init__(self, name):
        self.animal_name = name

    def eat(self):
        raise NotImplementedError("Child class should be implementing this")


class Monkey(Animal):
    def eat(self):
        print("Monkey eating bananas...")


class Bird(Animal):
    def eat(self):
        print("Bird eating seeds...")

    def fly(self):
        print("Bird soaring high...")


myMonkey = Monkey("Doug")
myMonkey.eat()

myBird = Bird("Tim")
myBird.fly()