


#Example 18:********************************** prime number or not*************************

 
val=int(input("enter a value to check is prime or not : "))
count=0
for i in range(2,val):
 if (val%i==0):
  count +=1
if (count==0):
 print("prime")
else:
 print("not prime") 