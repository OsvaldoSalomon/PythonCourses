my_list = [1, 2, 3, 4, 5, 6, 7]
print(my_list)

for element in my_list:
    print(element)

print(" ---------- ")

my_iter = iter(my_list)
print(my_iter)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print(" ---------- ")


def my_gen(x, y):
    for i in range(x):
        print("i is %d" % i)
        print("y is %d" % y)
        yield i * y


my_object = my_gen(10, 5)
print(type(my_object))
print(my_object)

print(" ------------ ")
print(next(my_object))
print(" ------------ ")
print(next(my_object))
print(" ------------ ")
print(next(my_object))

print(" ------------ ")

gen_exp = (x for x in range(5))

print(gen_exp)
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))

