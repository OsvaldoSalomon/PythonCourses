list1 = []
print(list1)

for i in range(10):
    result = i ** 2
    list1.append(result)

print(list1)

list2 = [x ** 2 for x in range(10)]
print(list2)

list3 = [x ** 2 for x in range(10) if x >= 5]
print(list3)

set1 = {x ** 2 for x in range(10)}
print(set1)

dict1 = {x: x ** 2 for x in range(10)}
print(dict1)

list3 = [x * 10 for x in range(11) if x >= 7]
print(list3)