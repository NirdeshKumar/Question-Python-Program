

# Sorting objects of user defined class in Python.


def sorting(n):
    for i in range(len(n)-1):
        for j in range(len(n)-1):
            if(n[j]>n[j+1]):
                temp=n[j]
                n[j]=n[j+1]
                n[j+1]=temp
                
a=int(input("enter a value: "))
b=[]
for y in range(a):
    val=int(input("enter a {} value: ".format(y)))
    b.append(val)
    
sorting(b)
print(b)
