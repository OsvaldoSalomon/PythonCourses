import re

a = "I enjoy learning programming languages such as Python 3"
print(a)
print(" ---------- ")

# \d digits. \s whitespaces, \w words

result = re.search(r"\D+", a)
print(result)
print(result.group())
print(" ---------- ")

result = re.search(r"\S+", a)
print(result)
print(result.group())
print(" ---------- ")

result = re.search(r"\W+", a)
print(result)
print(result.group())
print(" ---------- ")

print(a.index(result.group()))
print(" ---------- ")

result = re.search(r"\AI", a)
print(result.group())
print(" ---------- ")

result = re.search(r"3\Z", a)
print(result.group())
