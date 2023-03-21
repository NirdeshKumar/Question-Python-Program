

 


# Python | Program to print duplicates from a list of integers


a=[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
b=set()

for i in a:
    count=0
    for j in range(len(a)-1):
        if (i==a[j+1]):
            count +=1
    if(count>1):
        b.update([i])
print(list(b))
