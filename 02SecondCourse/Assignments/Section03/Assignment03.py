"""
Create a function called multi_merge that takes a list and a string
as arguments.
The function is supposed to return a merged list
containing the original list argument as well as each of the words that are
in the string argument elements in the list.

"""

def multi_merge(list_a, str):
    return list_a + str.split() + list(str)

print(multi_merge([1,2,3,4], "Hello there"))