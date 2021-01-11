s = 'django'
print(s[0])
print(s[-1])
print(s[0:4])
print(s[::-1])

#problem2
l = [3,7,[1,4,'hello']]
l[2][2]='goodbye'
print(l)
#problem3
d1={'simple_key':'hello'}
d2={'k1':{'k2':'hello'}}
d3={'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])
#problem
mylist=[1,1,2,2,3,4,3,3,3,5,6]
set(mylist)
print(mylist)
#5
age=4
name="komal"
print("Hello my  name is {a} and I am {b} years old".format(a= name,b=age))

