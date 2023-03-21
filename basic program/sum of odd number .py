

#Example 16:********************************** sum odd number*************************

val=int(input("enter a value : "))
sum=0
for x in range(1,val+1):
 if (x%2!=0):
  sum +=x
  print(sum)
 else:
  pass
print(sum)
