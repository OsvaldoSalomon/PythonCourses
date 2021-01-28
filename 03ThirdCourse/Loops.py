r = range(10)

for i in r:
    print(i * 2)

print(" -------- ")

vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]

for element_index in range(len(vendors)):
    print(vendors[element_index])

print(" -------- ")
for index, element in enumerate(vendors):
    print(index, element)

x = 1

# while x <= 10:
#     print(x)
#     x += 1
# else:
#     print("Out of the while loop. x is now greater than 10")

print(" -------- ")

while x <= 10:
    z = 5
    x += 1
    while z <= 10:
        print(z)
        z += 1

print(" -------- ")

list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        if j == 20:
            break
        print(i * j)
    print("Outside the nested loop")
