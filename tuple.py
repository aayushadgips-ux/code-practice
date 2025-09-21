from itertools import count, repeat

a=(1,2,3,4)
print(type (a))
b=(7,)
print(type(b))
c=(7)
print(type(c))
d=("aayush",1,7,"great")
print(type(d))
#tuple methods
e=a.count(3)
print(e)
f=a.index(1)
print(f)
repeat= a*3
print(repeat)
print(5 in a)
print(len(a))