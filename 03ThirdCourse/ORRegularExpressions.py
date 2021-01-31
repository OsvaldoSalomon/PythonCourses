import re

a = "I enjoy learning programming languages such as Python 3"

# A|B

result = re.search(r"\W(\w{2})\W|([A-Z]\w{5})\s\d", a)
print(result)
print(result.group(1))
print(result.group(2))
print(" -------- ")

result = re.search(r"\W(\w{50})\W|([A-Z]\w{5})\s\d", a)
print(result.group(1))
print(result.group(2))



