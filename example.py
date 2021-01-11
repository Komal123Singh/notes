n=int(input())
c=0
r=n
while n!=0:
    d=n%10
    n=n//10
    c=c+d*d*d
if c==r:
    print("armstrong")
else:
    print("no")
#factorial
n=int(input())
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))

#binary to decimal program
import math
n=int(input("Enter the binary number:"))
r=0
p=0
i=0

while n!=0:
    r=n%10
    n=int(n//10)
    p=p+r*math.pow(2,i)
    i=i+1
print("Decimal no:",int(p))

#Arary sum
list=[4,2,-3,1,8]
left=[3,4,6]
target=int(input("Enter a number:"))
def twosums(list,target):
    for i in range(len(list)):
        for j in range(list[i+1]):
            if list[i]+left[j]==target:
                return True
    return False
print(twosums(list,target))

#counting digit of a number
n=int(input("Enter a number:"))
count=0
while n!=0:
    count=count+1
    n=n//10
print("the no of digit in number is",count)




