my_list = ['b', 'd', 'a', 'z', 'x']
another_list = [1, 2, 3, 4, 5]

my_list.sort()
my_list.reverse()
another_list.reverse()

print(my_list)
print(another_list)

new_list = my_list[2:] + another_list[2:]
print(new_list)
