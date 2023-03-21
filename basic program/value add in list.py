


# WAP take a list by user and find the adding etc.

num = int(input("how many value enter in list : "))
list=[]
for i in range(num):
    val=int(input("enter value : "))
    list.append(val)

#adding new value

list.append(53)
print(list)

list.extend([22,443,12,435,66])
print(list)

list.insert(3,78)
print(list)

