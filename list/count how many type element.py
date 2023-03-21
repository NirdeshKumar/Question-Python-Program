
# WAP to add list element and insert in new list

num=int(input("How many value enter in list : "))
list=[]
list1=[]
add=0
list3=[]
for i in range(num):
    val=eval(input("enter value: "))
    list.append(val)


num=int(input("How many value enter in list : "))
for i in range(num):
    val=eval(input("enter value: "))
    list1.append(val)


print(list)
print(list1)

if (list<list1):
    for x in range(len(list)):
        add=list[x]+list1[x]
        list3.append(add)
    print(list3)        
else:
    for y in range(len(list1)):
        add=list[y]+list1[y]
        list3.append(add)
    print(list3)                   
