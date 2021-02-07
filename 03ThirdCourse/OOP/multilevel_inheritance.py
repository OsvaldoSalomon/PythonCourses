class Animal:
    def __init__(self, breed, color, weight):
        self.breed = breed
        self.color = color
        self.weight = weight

    def walk(self):
        print("I am walking")

    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")


class Dog(Animal):
    def bark(self):
        print("I am barking")


class PoliceDog(Dog):
    def __init__(self, breed, color, weight, hours_on_mission):
        super().__init__(breed, color, weight)
        self.hours_on_mission = hours_on_mission

    def detect_drugs(self):
        print("Sniff...sniff... I smell something here!")


class Cat(Animal):
    def meow(self):
        print("I am meowing")


if __name__ == "__main__":
    pass
class Animal:
    def __init__(self, breed, color, weight):
        self.breed = breed
        self.color = color
        self.weight = weight

    def walk(self):
        print("I am walking")

    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")


class Dog(Animal):
    def bark(self):
        print("I am barking")


class PoliceDog(Dog):
    def __init__(self, breed, color, weight, hours_on_mission):
        super().__init__(breed, color, weight)
        self.hours_on_mission = hours_on_mission

    def detect_drugs(self):
        print("Sniff...sniff... I smell something here!")


class Cat(Animal):
    def meow(self):
        print("I am meowing")


if __name__ == "__main__":
    airport_dog = PoliceDog("German Shepherd", "golden", 5000, 100)
    airport_dog.detect_drugs()
