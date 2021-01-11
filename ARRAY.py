#python program  to split an array amd add the firrst part to the end#
a=[3,5,6,7,8,9]
for i in range(len(a)):
    c=a[-1]
    a[0]=c
    print(a[i],end=" ")

#Interchanging first and last elements in a list
b=[5,6,7,8]

c=b[0]
b[0]=b[-1]
b[-1]=c
print(b)
#Python program to remove the occurencees of a list
f=[5,6,7,7,1,2,2,2,2,2,3,4,4,5,6,6,7]
print(list(set(f)))



def countZ(a,x):
    count=0
    for i in a:
        if (i==x):
            count=count+1
    return count
a=[2,2,2,2,5,6,7,1,1,11]
x=2
print(countZ(a,x))


#python program to find sum of a list
A=[3,4,5,4,5,6,7]
sum=0
for i in range(len(A)):
    sum=sum+A[i]
print(sum)

#python program to find multiplication of a list
A=[3,4,5,4,5,6,7]
sum=1
for i in range(len(A)):
    sum=sum*A[i]
print(sum)

#python program to find smallest no in a list
s=[3,5,6,7,1,2]
k=min(s)
for i in s:
    if i==k:
        print(min(s))
#python program to print all even numbers in a list
d=[5,4,3,1,3,8,9]
for i in d:
    if i%2==0:
        print(i)
#python progran to check if a string is palindrome or not
a1="mam"
a2=""
for i in a1:
    print()




