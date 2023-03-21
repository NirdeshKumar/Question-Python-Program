

# Write a Python program to find the average in a list.

a=[12,23,2,234,54,65,22,1,6,875,9]
summ=0
count=0
for x in a:
    summ += x
    count +=1
print('avg: ',summ/count)
