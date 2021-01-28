"""
Return the sum of the numbers in the array, except ignore sections of
numbers starting with a 7 and extending to the next 8
(every 7 will be followed by at least one 8).
Return 0 for no numbers.

EXAMPLE:
    sum78([1,2,2]) -> 5
    sum78([1,2,2,7,99,99,8]) -> 5
    sum78([1,1,7,8,2]) -> 5

"""


def sum78(nums):
    sum = 0
    in_range = False

    for i in range(len(nums)):
        if nums[i] == 7:
            in_range = True

        if in_range == False:
            sum += nums[i]

        if nums[i] == 8:
            in_range = False

    return sum


print(sum78([1, 2, 2]))
print(sum78([1, 2, 2, 7, 99, 99, 8]))
print(sum78([1, 1, 7, 8, 2]))
