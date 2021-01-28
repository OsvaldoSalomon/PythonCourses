# l=[1,2,3,4,5,6.5,"hello",['a','b','c']]
# l[6] ="Kello"
# print(l[6])
# print(l[7])
# print(l[::2])
# l.append('12')
# print(l)
#
# # To delete
# del l[2]
# print(l)
#
# l1=[1,2,3,4,5]
# minimum=min(l1)
# maximum=max(l1)
# print(minimum)
# print(maximum)
#
# l1.reverse()
# print(l1)
#
# sq=[]
# for i in range(1,11):
#     sq.append(i*i)
# print(sq)
#
# s=[i*i for i in range(1,11)]
# print(s)

# n=int(input("Enter n: "))
# l=[]
# for i in range(0,n):
#     val=int(input("Enter element: "))
#     l.append(val)
# print(l)

def linearsearch(k,lst):
    for val in lst:
        if k==val:
            return True
    else:
        return False


n = int(input("Enter n: "))
l = [int(input("Enter element: ")) for i in range(0, n)]
key = int(input("Enter key:"))

res=linearsearch(key,l)
print(res)
# n=int(input("Enter n: "))
# l=[int(input("Enter element: ")) for i in range(0,n)]
# print(l)
# for elem in l:
#     print(elem)

