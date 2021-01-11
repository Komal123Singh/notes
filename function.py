#1 function definition
nums = [1,1,1,2,4,3,4,1,2,3,4]
def arrayCheck(nums):
    for i in range(len(nums)):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    else:
        return False
print(arrayCheck(nums))

str = "hello"
result=0
def stringBits(str):
    for i in range(len(str)):
        if i%2==0:
            result =str[i] +str[0]
    return result
print(stringBits(str))

#*********************converting a list into string**************************************************************************
a=['sun','mon','tue']
li=' '.join(a)
print(li)
#***************************converting list into tuple**********************************************************************
listastuple=tuple(a)
print(listastuple)
#***********************************converting list into set*************************************************************************
lis=set(a)
print(lis)
#**********************program to  test a number is in defined range or not*******************************
def testrange(num):
    if num in range(0,10):
        print("num is in range")
    else:
        print("not in range")

testrange(566)
#*********************reverse a string ********************************************************************************************************
st="Hello"
a=' '
n=len(st)
while(n>0):
    a=a+st[n-1]
    n=n-1
print(a)

#********************************functiont to find sum of all numbers in a list************************************************************************************
a=[4,5,6,6,7,8,8,1,2,4,5]
sum=0
for i in range(len(a)):
    sum=sum+a[i]
print(sum)

print(7//2)