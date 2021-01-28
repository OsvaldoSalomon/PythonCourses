a = "Osvaldo Salomon"

# Position of the letter
print(a.index("v"))
print("\n----------------")

# Finds how many times an element is repeated
print(a.count("a"))
print("\n----------------")

# Search a sequence of characters and returns the index
print(a.find("al"))
print("\n----------------")

# Uppercase to lowercase
print(a.lower())
print(a.upper())
print("\n----------------")

# Checks if...
print(a.startswith("O"))
print(a.endswith("O"))
print("\n----------------")

b = "   Mary Shelby   "

print(b)

# Returns the string without spaces at the beginning or end
print(b.strip())
print("\n----------------")

c = "$$$Mary Shelby$$$"

print(c)
print("\n----------------")

# Returns the string without the specified character
print(c.strip("$"))
print("\n----------------")

# Replaces all the same characters for the others
print(c.replace("b", "l"))
print("\n----------------")

d = "Cisco,Juniper,HP,Avaya,Nortel"

# Extract each element from the string
print(d.split(","))
print("\n----------------")

# Insert a character in between two characters
print("_".join(a))
print("\n----------------")

first = "Dead"
second = "Pool"

print(first + second)

print(second * 3)
print("\n----------------")

print("D" in first)
print("X" in first)
print("\n----------------")

print("Cisco model: 2600XM, 2 WAN slots, IOS 12.4")

print("Cisco model: %s, %d WAN slots, IOS %f" % ("2800XM", 4, 15.4))
print("Cisco model: %s, %d WAN slots, IOS %.2f" % ("2800XM", 4, 15.4))
print("Cisco model: %s, %d WAN slots, IOS %.f" % ("2800XM", 4, 15.4))

print("\n----------------")
print("Cisco model: {}, {} WAN slots, IOS {}".format("2800XM", 4, 15.4))
print("Cisco model: {2}, {0} WAN slots, IOS {1}".format("2800XM", 4, 15.4))

print("\n----------------")
model = "2600XM"
slots = 4
ios = 12.4

print(f"Cisco model: {model}, {slots} WAN slots, IOS {ios}")
print(f"Cisco model: {model}, {slots * 2} WAN slots, IOS {ios}")
print(f"Cisco model: {model.lower()}, {slots * 2} WAN slots, IOS {ios}")
print("\n----------------")

"""
-----------
Slicing strings
-----------
"""

ipAddress = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"
print(ipAddress)
print(ipAddress[5:15])
print(ipAddress[5:])
print(ipAddress[:15])
print(ipAddress[:])
print(ipAddress[-9:-1])

print("\n-------------")

my_string = "0123456789"
print(my_string[4])
print(my_string[9])

#Goes 2 by 2
print(my_string[::2])
print(my_string[::3])
print(my_string[1::2])

# Odd characters that are less than 7
print(my_string[1:7:2])

