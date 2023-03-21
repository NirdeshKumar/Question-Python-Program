

 


# Python – Maximum and Minimum K elements without max function in list


a=[1,2,3,4,65,64,7,38,94,11,22,33,44,55]
b=a[0]
for i in a:
    if(i>b):
        b=i
print(b)  
