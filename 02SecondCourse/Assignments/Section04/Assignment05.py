"""
Define a method that accepts a list as an argument
and returns True if one the first 4 elements in the
list is a 6. The list may be less than 4.

first3([1,2,6,3,4]) -> True
first3([1,2,3,4,6]) -> False
first3([1,2,3,4,5]) -> False
"""


def first3(nums):
    end = len(nums)
    if end > 4:
        end = 4

    for i in range(end):
        if nums[i] == 6:
            return True

    return False


print(first3([1, 2, 6, 3, 4]))
print(first3([1, 2, 3, 4, 6]))
print(first3([1, 2, 3, 4, 6]))
print(first3([6]))
