

 


# Python –WAP to sorting list without sort function.

a=[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
for i in range(len(a)-1):
    for j in range(0,len(a)-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)
