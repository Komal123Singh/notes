
#program to interchange first and last element in a list
#def list(a):
    #n=len(a)
    #p=a[0]
    #a[0]=a[n-1]
    #a[n-1]=p
    #return a
#a =[2,3,4,5,6]
#print(list(a))
     ###OR###

#swap first and last value of a list
a=[1,4,5,6,7]
for i in range(len(a)):
    t=a[0]
    a[0]=a[-1]
    a[-1]=t
print(a)

#program to find length of a list
a=[3,45,7,8,9,12,0]
n=len(a)
print("the length of List is",n)
#program to check element is in  list or not
if (3 in a):
    print("element exists")
#program to clear a list
a.clear()
print(a)

#program to reverse a list
p =[3,5,6,7,8,9]
def reverse(p):
    return[i for i in reversed(p)]
print(reverse(p))

#count occurences of element in a list
def countX(a,x):
    count=0
    for  i in a:
        if(i==x):
            count=count+1
    return count
a =[3,4,5,6,7,8,5,6,7,5,4,3,7]
x=7
print('{} has occured {} times'.format(x,countX(a,x)))

#Find sum of elements in a list
sum=0
for i in range(0,n):
    sum=sum+a[i]
a = [3,4,5,6,7]
n=len(a)
print(sum)

#7 progran to find smallest no in list
a =[3,5,6,1,7,8]
z = min(a)
for i in a:
    if i==z:
        print(min(a))
#8 program for printing largest no
p = max(a)
for i in a:
    if i==p:
        print(max(a))

#9 program for printing second largest no
b =[1,2,3,8,9,10]
k = max(b)
for i in b:
    if i==k:
        b.remove(max(b))
print(max(b))


      #####OR###
#finding second largest value in a list
a.sort()
print(a[-2])

#10 program for printing even no in a list

w=[1,2,3,5,6,8,10,12]
e=[]
for i in w:
    if i%2==0:
        print(i,end=" ")

#program to print al the negative numbers in a list
s=[-1,3,-4,-5,7,89,-89]
for i in s:
    if i<0:
        print(i)

#program to remove duplicates
def repeat(x):
    repeated=[]
    n =len(x)
    for i in range(n):
        for j in range(i+1,n):
            if x[i]==x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
x=[1,2,3,4,1,2,2,3,4,5,6]
print(repeat(x))
#***********************OR####################################################################################3
#removing duplicate numbers from a list
A=[3,4,1,1,1,2,2,3,4,4,4,4,3,3,2]
print(list(set(A)))
#******************************************************************************************************************************************************************
#Fizz logic
l=int(input("Enter lower bound:"))
U=int(input("Enter upper bound:"))
for i in range(l,U):
    if i%3==0:
        print("Fizz",i)
    elif i%5==0:
        print("Buzz",i)
    elif i%3==0 and i%5==0:
        print("FizzBuzz",i)

#Decimal to binary
dec=23
print(oct(dec),"in octal")
print(hex(dec),"in hexadecimal")
#****************************************************************************
#Python program to find HCF or GCD
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
def gcd(a,b):
    if a==b:
        return a
    elif a%b==0:
        return b
    elif b%a==0:
        return a
    elif a>b:
        return gcd(a%b,b)
    else:
        return gcd(b%a,a)

ans=gcd(a,b)
print("GCD of a and b is : ",ans)

#Printing all permutations of a string
#Method 1: Using Inbuilt function
from itertools import permutations
for p in permutations('ABC'):
    print(p)
#Method 2: without inbuilt function
def toString(List):
    return''.join(List)
def permute(a,l,r):
    if l==r:
        print(toString(a))
    else:
        for i in range(l,r+1):
            k=a[l]
            a[l]=a[i]
            a[i]=k
            permute(a,l+1,r)
            k=a[l]
            a[l]=a[i]
            a[i]=k
string='ABC'
n=len(string)
a=list(string)
permute(a,0,n-1)
#Arithmetic expression evaluation











