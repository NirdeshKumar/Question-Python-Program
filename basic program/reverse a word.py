
# Write a program to print n natural number in descending order using a while loop.


x=1
c=[]
a = int(input("enter value: "))
for i in range(1,a+1):
    c.append(i)
c.reverse()
print(c)
