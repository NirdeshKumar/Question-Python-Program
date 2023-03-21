

#Example 4: Python program to check if a given number is an Armstrong number

#val=int(input("enter a number: "))

val=input("enter a number: ")
sum=0
p=int(val)
for i in val:
    m=int(i)
    product=m*m*m
    sum = sum+product
if (sum == p):
   print(f"{val} is a armstrong number.")
else:
    print(f"{val} is not armstrong number.")
