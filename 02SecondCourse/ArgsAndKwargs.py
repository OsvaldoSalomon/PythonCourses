def my_sum(*args):
    print(sum(args))


def key_value_func(**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs.get('name'))
    print(kwargs.get('address'))


key_value_func(name='mike', weight='200', age='27')

my_sum(10, 20, 12, 23, 3, 5, 63, 6)

# result = sum((1,2,3,4,5))
# print(result)
