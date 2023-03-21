

#  Write a Python script to merge two Python dictionaries. 
c={}
a={1:23,2:45,4:65,3:78}
b={9:54,"s":45,"t":23,"y":67}
for i in (a,b):
    c.update(i)
print(c)
