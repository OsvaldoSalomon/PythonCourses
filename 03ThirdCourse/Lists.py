list1 = ["Ava", "Benny", "Carlo", "Dave"]
print(list1)

list1[3] = "David"
print(list1)
print("\n")

list2 = [-11, 2, 12]
print(list2)
print(min(list2))
print(max(list2))
print("\n")

list3 = ["a", "b", "c"]
print(list3)
print(min(list3))
print(max(list3))
print("\n")

list4 = [1, 2, 3, "a", "b", "c"]
print(list4)
print(list4[0:3])
print(list4[2:])
print(list4[::2])
print(list4[::-1])
print(" --------- ")
list4.append(100)
print(list4)
del list4[4]
print(list4)
print(list4.pop(5))
print(list4)
list4.remove("c")
print(list4)
list4.insert(4, "b")
print(list4)
list4.insert(5, "c")
print(list4)
print(" --------- ")
print("\n")

list1.extend(list2)
print("list1.extend(list2) =", list1)
print("list1.count(2) =", list1.count(2))
print("\n")

print(list2)
list2.append(1)
list2.append(25)
list2.append(500)
print(list2)
list2.sort()
print("list2.sort() =", list2)
list2.reverse()
print("list2.reverse() =", list2)





