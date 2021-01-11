#creating own dictionary and find out the meaning
dict={'set':'well defined collection of objects','apple':'fruits','Brinjal':'vegetable','mutable':'Changeable'}
n=input("Enter a key value to find out the meaning: ")
if n in dict:
    print(dict[n])
else:
    print("Entered wrong value,this item is not present in dictionary")
#Design a faulty calculator
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=input("Enter an operator +,-,*,/ to perform operation")
if c=='+':
    if a==56 and b==9:
        print("Sum is",56)
    else:
        d=a+b
        print("Sum of a and b is",d)
elif c=='-':
    e=a-b
    print("Subtraction of a and b is",e)
elif c=='*':
    if a==45 and b==3:
        print("Multiplication is",555)
    else:
        f=a*b
        print("Multiplication is ",f)
elif c=='/':
    if a==56 and b==9:
        print("Division is",4)
    else:
        g=a/b
        print("Division is",g)
else:
    print("Wrong entry")
#3 Exercise :Guess the number
n=18
guess=1
print("No of guess is limited to 9 times")
while guess<=9:
    a=int(input("Enter any number"))
    if a<n:
        print("Enter greater number")
    elif a>n:
        print("Enter smaller number")
    else:
        print("You won")
        print("no of guess you took to finish",guess)
        break
    print(9-guess," :no of guess left")
    guess=guess+1
if(guess>9):
    print("Sorry Game over")

#4 Exercise :
n=int(input("Enter how many rows you want to print: "))
print("Type 1 or 0")
w=int(input("Enter 1 or 0"))
w=bool(w)
if w==True:
    for i in range(1,n):
        print('*'*i)
elif w==False:
    for i in range(n,0,-1):
        print('*'*i)

