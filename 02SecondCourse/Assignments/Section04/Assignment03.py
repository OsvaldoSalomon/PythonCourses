"""
Given a list of ints, return True if the sequence of number 1,2,3
appears in the list anywhere, false otherwise.

sequence([1,1,2,3,1]) -> True
sequence([1,1,2,4,1]) -> False
sequence([1,1,2,1,2,3]) -> True
sequence([1,2]) -> False
sequence([]) -> False

"""

def sequence(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False


print(sequence([1,1,2,3,1]))
print(sequence([1,1,2,4,1]))
print(sequence([1,1,2,1,2,3]))
print(sequence([1,2]))
print(sequence([]))
