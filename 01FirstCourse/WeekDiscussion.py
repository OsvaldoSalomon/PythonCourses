def division(a,b):
    try:
        result = a/b
    except:
        print("Division by zero")
    else:
        print("The division is:", result)

division(8,2)
division(8,0)

# ----------

my_number = 24

def multiply(x):
    try:
        result = x + my_number
    except TypeError:
        print("x is a wrong type.")
    else:
        print("Result is:", result)

multiply(2)
multiply('2')

# -----------

my_array = [1,2,3,4]

def array(z):
    try:
        print(my_array[z])
    except IndexError:
        print("The index you are trying to access is out of bounds")

array(2)
array(8)

