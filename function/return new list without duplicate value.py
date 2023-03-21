


# Write a Python function that takes a list and returns a new list without duplicate value.


def rem_dup(n):

    b=[]
    for i in n:
        if(i not in b):
            b.append(i)

    print(b)
n=[]
num=int(input("enter a store limit in list: "))
for i in range(num):
    val=int(input("enter a value: "))
    n.append(val)

rem_dup(n)
