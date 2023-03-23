


# Write a Python program to check if a dictionary is empty or not.

di={}
a={15:234,2:45,2:{1:1,2:2,3:3},14:165,3:78,12:{},4:45,5:234}
for x,y in a.items():
    if(y != {}):
        di.update([x])
print(di)
