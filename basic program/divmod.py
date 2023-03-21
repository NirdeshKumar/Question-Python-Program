


# WAP take a list by user and find the view etc.

num = int(input("how many value enter in list : "))
list=[]
for i in range(num):
    val=int(input("enter value : "))
    list.append(val)
print(list)
print("sum is : ",sum(list))
print("maximum: ",max(list))
print("Minimum ",min(list))
list.sort()
print("sorting list: ",list)
list.reverse()
print("Reverse list: ",list)
