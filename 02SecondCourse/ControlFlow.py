elephant = 800
hippo = 900
animal = "ape"

if elephant < hippo:
    print("elephant weighs less than hippo")
else:
    print("elephant is heavier than hippo")


if animal == "cow":
    print("Eats grass")
elif animal == "bird":
    print("Eats seeds")
elif animal == "monkey" or animal == "ape":
    print("Eats bananas")
else:
    print("We don't know what the animal eats")

count = 0

farm_animals = ('goat', 'horse', 'chicken', 'cow', 'dog')

for item in farm_animals:
    count = count + 1
    sentence = str(count) + " " + item + " is safe in our farm"
    print(sentence)

