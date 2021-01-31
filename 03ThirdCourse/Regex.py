import re

my_string = "You can learn any programming language, whether it is Python2, Python3, Perl, Java"
print(my_string)
print(" -------- ")

# a = re.match(pattern, string, optional flags)
a = re.match("You", my_string)  # checking if the characters "You" are indeed at the beginning of the string
print(a)
print(" -------- ")

a = re.match("abc", my_string)
print(a)
print(type(a))
print(" -------- ")

a = re.match("You", my_string)
print(a)
print(
    a.group())  # result is 'You'; Python returns the match it found in the string according to the pattern we provided
print(" -------- ")

a = re.match("you", my_string, re.I)  # re.I is a flag that ignores the case of the matched characters
print(a)
print(a.group())
print(" -------- ")

# a = re.search(pattern, string, optional flags) general search syntax; searching for a pattern throughout the entire
# string; will return a match object if the pattern is found and None if it's not found
arp = "22.22.22.1   0    b4:a9:5a:ff:c8:45 VLAN#222     L"
print(arp)
b = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)
print(b)
print(b.group(1))
print(b.group(2))
print(b.group(3))
print(b.group(4))
print(b.group())
print(b.group(0))
print(" -------- ")

# Regular Expressions - the "re.findall" and "re.sub" methods
c = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)
print(c)
c = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)
print(c)
print(" -------- ")
arp = "22.22.22.1   0    b4:a9:5a:ff:c8:45 VLAN#222     10.10.10.10   L"
print(arp)
c = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)
print(c)
print(" -------- ")
arp = "22.22.22.1   0    b4:a9:5a:ff:c8:45 VLAN#222     L"
print(arp)
d = re.sub(r"\d", "7", arp)
print(d)
