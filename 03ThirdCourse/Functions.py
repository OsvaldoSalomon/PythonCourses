def my_first_function():
    """This is my first function!"""
    print("Hello Python!")


my_first_function()

print(" ------------ ")


def my_function(x):
    print(x)


my_function("Hello World")

print(" ------------ ")


def function_two(x, y):
    print("Hello " + x)
    print("Hello " + y)


function_two("Python", "Java")

print(" ------------ ")


def my_sum(x, y):
    sum = (x + y)
    print(sum)


my_sum(4, 5)

print(" ------------ ")


def my_operation(x, y, z=3):
    sum = (x + y) * z
    print(sum ** 2)


my_operation(2, 4, 7)

print(" ------------ ")


def function_one(x, *args):
    print(x)
    print(args)


function_one("Hey")
function_one("Hey", 100, 200)

print(" ------------ ")


def function1(x, *args):
    print(x)
    for argument in args:
        print(argument)


function1(1, 2, 3)
