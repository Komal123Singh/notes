#armstrong number
c = int(input())
r=0
n=c
while n!=0:
    d=n%10
    n=n//10
    r=r+d**3
if c==r:
    print("armstrong")
else:
    print("not armstrong")

#Even odd number
a =int(input())
if a%2==0:
    print("even")
else:
    print("odd")


#6 apphabet pattern
for i in range(1,6):
    for j in range(65,65+i):
        print(chr(i),end='')
    print()
#prime no
n = int(input())
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("no is not prime")
            break
    else:
        print("no is prime")
#range for printing prime no
a = 10
b = 20
for c in range(a,b):
    if i>1:
        for i in range(2,c):
            if c%i==0:
                break
        else:
            print(c,end=' ')
print("\n")
#factorail no
n=int(input("Enter a number to find factorial of a number:"))
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))
#fibonacci
a=-1
b=1
n = int(input("enter a range"))
for i in range(n):
    c = a+b
    print(c,end=" ")
    a=b
    b=c
print("\n")
#sum of digits
c = 0
n = int(input("enter a three digit number"))
for i in range(n):
    d = n%10
    n = n/10
    c = c+d
print(int(c))
print("\n")
#sum of array
a=[2,4,6,7,8,9]
for i in range(a):
#7 palindrome

s=int(input("Enter a number"))
n=s
r=0
while n!=0:
    d=n%10
    n=n//10
    r=r*10+d
if s==r:
    print("palindrome")
else:
    print("not palindrome")

#sum of natural numbers
a = 1
b = 6
c=0
for i in range(a,b):
    c=c+i
print(c)

