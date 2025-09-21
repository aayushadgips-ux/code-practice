#LIST
a= ["aayush",300,56,"great"]

print(a[1])
a[1]= "400" #unlike strings lists are mutable
print(a[1])
print(a[1:4])
#methods
a.append("greatest")
print(a)

b=[45,65,77,88,5,5,4,65,43]
b.sort()
print(b)
b.remove(4)
print(b)
b.reverse()
print(b)
b.insert(3,57777774)
print(b)
b.pop(2)
print(b)
print(b.pop(2))
