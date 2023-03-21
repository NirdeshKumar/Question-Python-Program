
# WAP to separate positive and negative number from a list.


q=[]
x=0
c=[]
d=[]
a=int(input("enter a value: "))
for i in range(a):
    val=int(input("enter a value: "))
    q.append(val)

while(x<len(q)):
    if(q[x]>=0):                                          
        c.append(q[x])
    else:
        d.append(q[x])
    x += 1
print(c)
print(d)
