s={1,2,3,4,5,"aaa"}
print(s)

s1=input("Enter string: ")
cnt=0
spcl_chars={"!","@","$","#","%","^","&","*","(",")","-","_","=","+"}

for ch in s1:
    if ch in spcl_chars:
        cnt=cnt+1
print(cnt)

s2={1,2,3,4,5}
s3={2,3,6,7}

print(s2.union(s3))
print(s2.intersection(s3))
print(s2.isdisjoint(s3))