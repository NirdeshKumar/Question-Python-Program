


# WAP take a list by user and find the adding etc.

num = int(input("how many value enter in list : "))
list=[]
for i in range(num):
    val=int(input("enter value : "))
    list.append(val)

#delete

list.pop()
print(list)

list.pop(3)
print(list)

list.remove(6)
print(list)

list.clear()
print(list)

new=list.copy()
print(index(53))


del list
print(list)
print(new)
