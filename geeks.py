#1 program to print AsCII value of a character
n = input()
print(ord(n))

#2 program for printing squares of n natural numbers
n = int(input())
c = 0
for i in range(1,n+1):
    c = c+(i*i)
print(c)

#3 progran for finding sum of array
def _sum(arr,n):
    return(sum(arr))
arr = []
arr = [1,2,3,4,5,6,7]
n = len(arr)
ans=_sum(arr,n)
print("the sum of array is:",ans)

#4 program to find largest element in array
def large(a,n):
    max = a[0]
    for i in range(1,n):
        if a[i]>max:
            max=a[i]
    return max
a =[1,2,3,9,4,5]
n = len(a)
ans = large(a,n)
print("this is large no",ans)

#split array
def splits(a,n):
    for i in range(0,n):
        print(a[i],end=" ")
a=[3,5,6,7,8,9]
n=len(a)
splits(a,n)
#python program to find common letters in a string
b="komalsingh"
c="shanvikumari"
e=list(set(b)&set(c))
print("common letters are:")
print(e,end=" ")
print("\n")

#removing duplicate numbers from a list
A=[3,4,1,1,1,2,2,3,4,4,4,4,3,3,2]
print(list(set(A)))