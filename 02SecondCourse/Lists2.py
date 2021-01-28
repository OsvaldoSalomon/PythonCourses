my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'orange', ['John', 'Robert'], 'banana'], 'd', 'c', 'c']
my_list[6][2][1] = 'Joe'
print(my_list)

idx_pos = my_list.index('c')
print(idx_pos)

c_count = my_list.count('c')
print(c_count)

