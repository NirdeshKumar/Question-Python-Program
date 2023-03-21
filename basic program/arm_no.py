val=input("enter a number: ")
p=val
sum=0
for i in val:
    m=int(i)
    product=m*m*m
    sum = sum+product
print(sum)
print(p)
if(p==sum):
    print(f"{val} is a armstrong number.")
else:
    print(f"{val} is not armstrong number.")
