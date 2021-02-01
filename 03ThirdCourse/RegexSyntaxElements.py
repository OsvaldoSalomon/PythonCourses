import re

a = "I enjoy learning programming languages such as Python 3"

print(re.search(r"^[A-Z]\s\w{5}", a))
print(" ---------- ")

print(re.search(r"[A-Z]\w{5}\s\d$", a))
print(" ---------- ")
print("\n")

x = "He is ... zzzzzzzzzz . . . sleeeeeeping"
print(x)
print(re.search(r"z{10}", x))
print(" ---------- ")

print(re.search(r"z{1,}", x))
print(" ---------- ")

print(re.search(r"z{1,10}", x))
print(" ---------- ")

print(re.search(r"z{1,10}?", x))
print(" ---------- ")

print(re.search(r"z{3,10}?", x))
print(" ---------- ")

