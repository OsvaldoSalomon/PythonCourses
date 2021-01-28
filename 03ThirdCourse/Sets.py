list4 = [1, 2, 3, 4, 5, 2, 3]
print(list4)

print(set(list4))

set1 = {11, 12, 13, 15, 14, 15, 15, 11}
print(set1)
print(type(set1))
print(len(set1))

print(11 in set1)
print(10 in set1)
print(10 not in set1)

set1.add(16)
print(set1)

print("\n")

set2 = {1, 2, 3, 4}
set3 = {3, 5, 8}
print(set2)
print(set3)
print(" ----------- ")

print(set2.intersection(set3))
print(set3.intersection(set2))
print(set2.difference(set3))
print(set3.difference(set2))
print(" ----------- ")

print("set2.union(set3) =", set2.union(set3))

print("\n")
print(" -------------- ")

print("Frozensets")

list1 = [1, 2, 3, 4]
list2 = [3, 4, 7]

print(list1)
print(list2)

fs1 = frozenset(list1)
fs2 = frozenset(list2)

print(fs1)
print(fs2)
print(type(fs1))

