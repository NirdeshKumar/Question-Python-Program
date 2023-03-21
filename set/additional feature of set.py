
# **************************************** ADDITIONAL FEATURE OF SET ********************************************


a=set()
b=set()
a.add(98)
#print(a)
a.update([12,34,56,78])
#print(a)

b.add(1)
b.update([2,3,4,56,78,8])

print(a|b)
print(a.union(b))

print(a.intersection(b))
print(a&b)

print(a.difference(b))
print(a-b)

print(b.difference(a))
print(b-a)

print(a.symmetric_difference(b))
print(a^b)
