
# Write a program to print n natural number in descending order using a while loop.


x=1
c=[]
a = int(input("enter value: "))
while(x<=a):
    c.append(x)
    x +=1
c.reverse()
print(c)
