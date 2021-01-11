#Factorial
n=3
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(n))

#armstrong
n=153
s=n
r=0
while n!=0:
    d=n%10
    n=n//10
    r=r+d*d*d

if s==r:
    print("Armstrong")
else:
    print("not armstrong")
#Palindrome
n=163
p=n
r=0

while n!=0:
    d=n%10
    n=n//10
    r=r*10+d
if p==r:
    print("palindrome")
else:
    print("not palindrome")

#prime number
n=int(input("enter a number: "))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(" not prime")
            break
    else:
        print(" prime")

