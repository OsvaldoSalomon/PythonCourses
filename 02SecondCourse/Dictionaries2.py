dict = {'John': 190, 'Robert': 165, '99': 'some data', 'items': ['orange', {'k1': 'some value'}], 'tuple': (1,2,3,4,5)}
print(dict['items'][1])
my_tuple = dict['tuple']
print(my_tuple)
print(dict)
dict.pop('tuple')
print(dict)