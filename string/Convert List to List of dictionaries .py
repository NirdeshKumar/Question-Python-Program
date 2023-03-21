

 


# Python – Convert List to List of dictionaries


a=[1,'asd',34,'eee','rty']
b=[2,4,5,6,7]
new={}
for x,y in zip(a,b):
    new[x]=y
print(new)      
