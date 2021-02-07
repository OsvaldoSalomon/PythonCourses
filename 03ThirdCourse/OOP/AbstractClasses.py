from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, breed, color, weight):
        self.breed = breed
        self.color = color
        self.weight = weight

    def walk(self):
        print("I am walking")

    @abstractmethod
    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")


class Dog(Animal):
    def bark(self):
        print("I am barking")

    def eat(self):
        print("I am eating like a dog!")

    def __eq__(self, other):
        return type(self) == type(other) and self.weight == other.weight

    def __ne__(self, other):
        return type(self) == type(other) and self.weight != other.weight

    def __str__(self):
        return f"I am a dog of {self.breed} breed, my fur color is {self.color} and I weigh {self.weight}"


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


class IEmail(ABC):
    @abstractmethod
    def send(self):
        pass

    @property
    @abstractmethod
    def valid_domain(self):
        pass


class Email(IEmail):
    def send(self):
        print(f"Sending an email from the Email class with the valid domain {self.valid_domain}")

    valid_domain = "epicpython.io"


if __name__ == "__main__":
    blue_cat = Cat("Bristish ShortHair", "blue", 2000)
    golden_dog = Dog("Golden Retriever", "golden", 5000)
    french = Dog("French Bulldog", "brown", 2000)
    golden_dog2 = Dog("Golden Retriever", "golden", 2000)

    print("golden_dog != golden_dog2:", golden_dog != golden_dog2)
    print("french == golden_dog2:", french == golden_dog2)
    print("french != golden_dog2:", french != golden_dog2)

    print("golden_dog2 == blue_cat:", golden_dog2 == blue_cat)

    print(" --------- ")

    print(golden_dog2)

    print(" --------- ")

    french.eat()
    blue_cat.eat()

    email = Email()
    email.send()
