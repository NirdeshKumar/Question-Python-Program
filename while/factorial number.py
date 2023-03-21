
# WAP to print prime number

#num=int(input("enter a value : "))


x=1
c=[]
while(x<=100):
    i=2
    count=0    
    while(i<x):
    #for i in range(2,x):
        if (x%i==0):
            count +=1
        i += 1
    if(count==0):
        print(x)
        c.append(x)
      
    x += 1
print("\n\nsum prime number: ",sum(c))
