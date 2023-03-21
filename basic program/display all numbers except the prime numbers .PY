

#Example 5: Python program to count the number of even and odd numbers from a series of numbers.

m=int(input("count loop: "))
for i in range(m):
    val=int(input("enter a number: "))
    count=0
    s=0
    for x in range(2,val+1,2):
        count += 1
    print(count)
    for var in range(1,val+1,2):
        s += 1
    print(s)    
