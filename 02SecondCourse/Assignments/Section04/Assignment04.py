"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

grow_string('Code') -> 'CCoCodCode'
grow_string('abc') -> 'aababc'
grow_string('ab') -> 'aab'
"""

def grow_string(str):
    result = ""
    for i in range(len(str)):
        result = result + str[:i + 1]
    return result


print(grow_string('Code'))
print(grow_string('abc'))
print(grow_string('ab'))
print(grow_string('Osvaldo'))

