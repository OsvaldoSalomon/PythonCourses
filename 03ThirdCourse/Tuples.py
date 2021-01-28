my_tuple = ()
print(type(my_tuple))

my_tuple = (9)
print(type(my_tuple))

my_tuple = (9,)
print(type(my_tuple))
print(" ----------- ")

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

print(my_tuple[0]) #returns the first element in the tuple (index 0)
print(my_tuple[-1]) #returns the last element in the tuple (index -1)
print(my_tuple[0:2]) #returns (1, 2)
print(my_tuple[:2]) #returns (1, 2)
print(my_tuple[1:]) #returns (2, 3, 4)
print(my_tuple[:]) #returns (1, 2, 3, 4)
print(my_tuple[:-2]) #returns (1, 2)
print(my_tuple[-2:]) #returns (3, 4)
print(my_tuple[::-1]) #returns (4, 3, 2, 1)
print(my_tuple[::2]) #returns (1, 3)

print(" ----------- ")

tuple1 = ("Cisco", "2600", "12.4")
(vendor, model, ios) = tuple1
print(tuple1)
print(vendor)
print(model)
print(ios)

print(" ----------- ")

(a, b, c) = (10, 20, 30)
print(a)
print(b)
print(c)

print(" ----------- ")

# Tuples - immutable
# List - mutable

a = ()
b = []
print("a = () :", type(a))
print("b = [] :", type(b))

print(" ----------- ")

print(len(my_tuple))
print(max(my_tuple))
print(min(my_tuple))

print(" ----------- ")
print("my_tuple =", my_tuple)
my_tuple += (6, 7, 8)
print("my_tuple += (6, 7, 8) =", my_tuple)
my_tuple = my_tuple * 2
print("my_tuple = my_tuple * 2 =", my_tuple)


