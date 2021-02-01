import re

a = "I enjoy learning programming languages such as Python 3"

print(re.split(r" ", a))
print(re.split(r"\s", a))
print(a.split())
print(" ----------- ")

print(re.split(r"\W\w{2}\W", a))
print(" ----------- ")

print(re.subn(r"\s", "_", a))

