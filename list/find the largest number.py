

# Write a Python program to find the largest number in a list.


a=[12,23,2,234,54,65,22,1,6,875,9]
large=a[0]
for i in a:
    if(large<i):
        large=i
print(large) 
