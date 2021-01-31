import re

a = "I enjoy learning programming languages such as Python 3"
print(a)
print(" ---------- ")

result = re.findall(r"[a-z]", a)
print(result)
print(" ---------- ")

result = re.findall(r"[A-Z]", a)
print(result)
print(" ---------- ")

result = re.findall(r"[a-f]", a)
print(result)
print(" ---------- ")

result = re.findall(r"[abn]", a)
print(result)
print(" ---------- ")

result = re.findall(r"[^a]", a)
print(result)
print(" ---------- ")

result = re.findall(r"[0-9]", a)
print(result)
print(" ---------- ")


