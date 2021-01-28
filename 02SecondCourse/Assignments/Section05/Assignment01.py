"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.

After creating the class hierarchy create instances of each of the 3 animals
dog, fish and bird and make them eat and move.

"""


class Animal:
    def __init__(self):
        print("Animal Constructed")

    def move(self):
        print("Animal is moving...")

    def eat(self):
        print("Animal is Eating...")


class Bird(Animal):
    def __init__(self, bird_age, bird_name):
        Animal.__init__(self)
        self.age = bird_age
        self.name = bird_name

    def move(self):
        print("Bird is flying...")


class Fish(Animal):
    def __init__(self, fish_age, fish_name):
        Animal.__init__(self)
        self.age = fish_age
        self.name = fish_name

    def move(self):
        print("Fish is swimming...")


class Dog(Animal):
    def __init__(self, dog_age, dog_name):
        Animal.__init__(self)
        self.age = dog_age
        self.name = dog_name

    def move(self):
        print("Dog is running...")


my_dog = Dog(3, 'Wolfy')
my_dog.move()
my_dog.eat()

my_fish = Fish(1, 'Nemo')
my_fish.move()
my_fish.eat()

my_bird= Bird(4, 'Birdy')
my_bird.move()
my_bird.eat()
