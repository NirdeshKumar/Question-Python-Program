

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)

a={}
b=int(input("enter value: "))
for i in range(b):
    a[i]=i**2
print(a)
