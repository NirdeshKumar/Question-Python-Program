

 
# Ways to remove i’th character from string in Python

a=input()
new=''
for y in a:
    if(y != 'i'):
        new=new+y
print(new)    

#-------------- OR ------------------------------------

a=input("enter the string:").split()
for i in a:
    for j in i:
        if(j!="i"):
            print(j,end="")
