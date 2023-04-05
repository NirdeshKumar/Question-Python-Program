

# Perfect Number

num=int(input("enter a value: "))
add=0
for i in range(1,num):
    if(num%i==0):
        add += i
if(add==num):
    print("yes perfect number")
else:
    print("no")
