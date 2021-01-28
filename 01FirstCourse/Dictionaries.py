d={1:"Sam",2:"Rita",3:"John",4:"Regan",5:"Sam"}
d2={6:"Eddie",7:"Harper"}
d3={}
print(d)
print(d2)

d.update(d2)
d3=d.copy()

print(d3)
print(d.keys())
print(d.values())
print(d.items())

print(d.get(4))

d4={}
t=(1,2,3,4,5)
d4=d4.fromkeys(t,0)
print(d4)

d5={1:"a",2:"B",3:"C"}

if "B" in d5:
    print("Yes")
else:
    print("No")

d6={1:"Sam",2:"Rita",3:"John",4:"Regan",5:"Flynn"}
for keys in d6:
    print("Rollno:", keys)
    print("Name", d6[keys])
    print()

