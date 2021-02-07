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

    def eat(self):
        print("I am eating like a dog!")


class DetectDrugsMixing:
    def detect_drugs(self):
        print("I am detecting some drugs here!")


class PoliceDog(Dog, DetectDrugsMixing):
    def __init__(self, breed, color, weight, hours_on_mission):
        super().__init__(breed, color, weight)
        self.hours_on_mission = hours_on_mission


class Cat(Animal):
    def meow(self):
        print("I am meowing")

    def eat(self):
        print("I am eating like a cat!")


def make_animal_eat(animal):
    animal.eat()


if __name__ == "__main__":
    blue_cat = Cat("Bristish ShortHair", "blue", 7000)
    golden_dog = Dog("Golden Retriever", "golden", 5000)

    make_animal_eat(blue_cat)
    make_animal_eat(golden_dog)
