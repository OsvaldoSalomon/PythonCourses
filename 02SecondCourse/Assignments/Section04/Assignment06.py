"""
Create a method called last2 that accepts a string argument.
The method should return the count of the number of times that the last
2 characters appear in the rest of the string. You should not count
the last 2 characters as an occurrence. The last 2 characters is just the
sequence your method should look for in the remaining string.

So "hixxxhi" yields 1 (we won't count the end substring).

last2("hixxxhi") -> 1
last2("xaxxaxaxx") -> 1
last2("axxxaaxx") -> 2

"""


def last2(str):
    if len(str) <= 2:
        return 0

    last2 = str[len(str) - 2:]
    count = 0

    for i in range(len(str) - 2):
        sub = str[i: i + 2]
        if sub == last2:
            count = count + 1

    return count


print(last2("hixxxhi"))
print(last2("xaxxaxaxx"))
print(last2("axxxxaaxx"))
