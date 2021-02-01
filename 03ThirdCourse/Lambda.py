# lambda arg1, arg2, ... arg n: an expression using the arguments

a = lambda x, y: x * y

print(a)
print(type(a))

print(a(2, 10))
print(a(5, 50))


def myfunc(mylist):
    list_xy = []
    for x in range(10):
        for y in range(5):
            result = x * y
            list_xy.append(result)
    return list_xy + mylist


print(myfunc([100, 101, 102]))

b = lambda mylist: [x * y for x in range(10) for y in range(5)] + mylist

print(b)
print(b([100, 101, 102]))