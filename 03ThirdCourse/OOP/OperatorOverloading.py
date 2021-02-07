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

# Most common Magic Methods

# Addition(+): __add__(self, other)
#
# Subtraction(-): __sub__(self, other)
#
# Multiplication(*): __mul__(self, other)
#
# Floor division( //): __floordiv__(self, other)
#
# True division( /): __truediv__(self, other)
#
# Modulo( %): __mod__(self, other)
#
# Power(**): __pow__(self, other)
#
# Less than( <): __lt__(self, other)
#
# Greater than( >): __gt__(self, other)
#
# Less than or equal( <=): __le__(self, other)
#
# Greater than or equal( >=): __ge__(self, other)
#
# Equals( ==): __eq__(self, other)
# 
# Not equals( !=): __ne__(self, other)
