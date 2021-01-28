s = "Hello"
if "ell" in s:
    print("Present")
else:
    print("Not present")


if "book"<"cat":
    print("Smaller")
else:
    print("bigger")

print(s[1:4])

s1=s[0:5:2]
print(s1)


str='       H      .'
print(str.lstrip())

x=input("Enter string: ")
for ch in x:
    print(ch)

y=input("Enter string: ")
for i in range(0,len(y)):
    print(y[i])


b=input("Enter string: ")
ncount=0
acount=0
scount=0
for ch in b:
    if ch.isdigit():
        ncount=ncount+1
    elif ch.isalpha():
        acount=acount+1
    elif ch.isspace():
        scount=scount+1
    else:
        continue

print(ncount)
print(acount)
print(scount)

