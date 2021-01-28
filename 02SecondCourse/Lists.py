my_list = [1, 2, 3, 4, 5]
my_list.append("This is a sentence")
my_list[0] = ["hello", "hey"]
my_list.pop()
print(my_list)

my_list = [1, 2, 3, 4, 5]
my_list.append([6, 7, 8, 9])
print(my_list)

my_list = [4, 3, 1, 5, 2]
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)

my_list = ['c', 'd', 'a', 'b', 'z']
print(my_list)
my_list.sort()
print(my_list)
print(my_list[-1])

item_count = len(my_list)
print(item_count)

my_list = [1, 2, 3, 4, 5]
another_list = ['a', 'b', 'c', 'd', 'e']
new_list = my_list + another_list
print(new_list)