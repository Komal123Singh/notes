#Inheritance
class fruit:
    def __init__(self):
        print("This is a fruit")
class citrus(fruit):
    def __init__(self):
        super().__init__()
        print("I m citrus")
lemon=citrus()

#program to check if a string is palindrome or not
x="malayalam"
b=x[::-1]
print(str(b))
if x==b:
    print("yes")
else:
    print("No")
#length of a string
w=len(x)
print(w)

#program to check a substring is present or not
def check(string,sub_str):
    if(string.find(sub_str)==-1):
        print("No")
    else:
        print("Yes")
string="geeks for geeks"
sub_str="geeks"
check(string,sub_str)


#List programs
# program to sort python dictionaries by Key or value
x={'koaml':2,'wer':1,'rty':20}
sum=0
for i in x.values():
    sum=sum+i
print(sum)

#remove a key from dictionary
del x['wer']
print(x)
#find common elements using dictionary intersect

d1=[1,5,6,7,8]
d2=[3,7,89,90]
d3=[89,90,94,95]
for i in d1,d2,d3:
    if d1[i]=d2[i]=d3[i]:


