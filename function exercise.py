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
#*****************************************creating empty numpy array*****************************
import numpy as np
np.array([])