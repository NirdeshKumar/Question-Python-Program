


# Write a Python program to remove duplicates value from the dictionary.


a={15:234,2:45,14:165,3:78,4:45,5:234}
print(a)
num={}
for x,y in a.items():
    if(y  not in num.values()):
        num[x]=y
print(num)
