
# WAP to add only integer value in a list

num=int(input("How many value enter in list : "))
list=[]
add=0
for i in range(num):
    val=eval(input("enter value: "))
    list.append(val)
for y in list:
    if(type(y)==int or type(y)==float):
        add +=y
print(add)      

