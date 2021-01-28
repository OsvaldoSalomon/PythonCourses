"""
Given2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the
same place in both strings.

Example:
    string_match('xxcaazz', 'xxbaaz') -> 3
    string_match('abc', 'abc') -> 2
    string_match('abc', 'axc') -> 0
"""


def string_match(a,b):
    # Figure out which string is shorter
    shorter = min(len(a), len(b))

    count = 0

    for i in range(shorter - 1):
        a_sub = a[i: i+2]  # gives substring of size 2
        b_sub = b[i: i+2]
        if a_sub == b_sub:
            count = count + 1
    return count


print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))