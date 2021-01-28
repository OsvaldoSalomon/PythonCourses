def helloWorld():
    print("Hello world!")

for i in range(0,5):
    helloWorld()

def sumOfTwo(n1,n2):
    sum =n1+n2
    print("Sum:", sum)
    return sum

num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))

s=sumOfTwo(num1,num2)
print(s)


def sumOfTwo2(*nums):
    sum = 0
    for n in nums:
        sum = sum+n
    return sum

s3=sumOfTwo2(1)
s1=sumOfTwo2(1,2)
s2=sumOfTwo2(1,2,3)

print("s3",s3)
print("s1",s1)
print("s2",s2)