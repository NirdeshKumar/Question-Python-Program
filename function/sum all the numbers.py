

# Write a Python function to sum all the numbers in a list.


def add(n):
    count=0
    for j in n:
        count +=j
    print(count)
        
a=int(input("enter a value: "))
b=[]
for y in range(a):
    val=int(input("enter a {} value: ".format(y)))
    b.append(val)

add(b)
