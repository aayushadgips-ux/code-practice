# set
e=set()# e={} is not empty set
print(type(e))
# methods
s= {1,45,76,43,34,54,"aayush"}
print(type(s))
s.add(44)
s.remove(34)
print(s)
#union
a1={1,2,3,4,5,6,7}
a2={0,9,8,7,6,5,4}
print(a1.union(a2))
print(a1.intersection(a2))
print(len(a1))
print({1,2}.issubset(a1))
print(a1.clear())