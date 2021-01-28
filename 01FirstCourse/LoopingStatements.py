n = int(input("Enter n: "))
for i in range(1, n+1):
    print(i)
print("Done.")

# ------------------

ch=1
while ch==1:
    print("Repeat")
    ch=int(input())
print("Sayonara")

# ---------

num=int(input("Enter num: "))
sum=0
while num !=0:
    rem=num%10
    sum=sum+rem
    num=num//10
print(sum)