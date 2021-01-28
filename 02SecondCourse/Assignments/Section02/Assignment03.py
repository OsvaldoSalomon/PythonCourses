original_list = ['cup', 'cereal', 'milk', (8, 4, 3)]
print(original_list[3])

n1 = original_list[3][0]
n2 = original_list[3][1]
n3 = original_list[3][2]

new_list = [n1, n2, n3]
new_list.sort()
new_tuple = (new_list[0], new_list[1], new_list[2])
original_list.pop()
original_list.append(new_tuple)
print(new_list)
print(new_tuple)
print(original_list)
