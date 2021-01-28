"""
Define a function called key_list_items that can accept an unlimited number
of lists along with another argument. The function should return the second to last item
in the specific list specified by the user of the function.

Example:
    For example, the code below function call should return: jan

    key_list_items("people", things=['book','tv'], people=['pete','mike','jan','tom'])
"""


def key_list_items(key, **kwargs):
    keys = kwargs[key]
    print(keys[-2])


key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'])
