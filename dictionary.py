# https://training-git.chetu.com/Chetu-India/Python-bt-Feb23-nirdeshkumar9759.git
'''
# Write a Python to add a key to a dictionary.
a={0: 10, 1: 20}
a[2]=30
a.update({3:40,4:50})
print(a)
'''
'''
# Write a Python script to concatenate the following dictionaries to create a new one.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic={}
for i in (dic1,dic2,dic3):
    dic.update(i)
print(dic)    
'''
'''
# Write a Python script to generate and print a dictionary that contains a number(between 1 and n) in the form (x, x*x)

a={}
b=int(input("enter value: "))
for i in range(1,b):
    a[i]=i**2
print(a)
'''
'''
#  Write a Python script to merge two Python dictionaries. 
c={}
a={1:23,2:45,4:65,3:78}
b={9:54,"s":45,"t":23,"y":67}
for i in (a,b):
    c.update(i)
print(c)

'''

# Write a Python program to remove a key from a dictionary.
'''
a={9:54,"s":45,"t":23,"y":67,"z":746,"x":54}
a.pop("s")
print(a)
'''

# Write a Python program to map two lists into a dictionary.
'''
a=['a','b','c','d','e','f','g']
b=['A','B','C','D','E','F','G']
c={}
for i,j in zip(a,b):
    c[j]=i
print(c)
'''
'''
c=[]
l=[]
m={}
a={15:234,2:45,14:165,3:78}
b=a.keys()
d=a.values()

for i in d:
    l.append(i)

for i in b:
    c.append(i)

for x in range(len(c)):
    for y in range(x+1,len(c)):
        if(c[x]>c[y]):
            temp=c[x]
            c[x]=c[y]
            c[y]=temp
for e,f in zip(l,c):
    m[f]=e
print(a)
print(m)
'''

# Write a Python program to remove duplicates from the dictionary.

'''
a={15:234,2:45,14:165,3:78,4:45,5:234}
print(a)
num={}
for x,y in a.items():
    if(y  not in num.values()):
        num[x]=y
print(num)
'''

# Write a Python program to check if a dictionary is empty or not.

di={}
a={15:234,2:45,2:{1:1,2:2,3:3},14:165,3:78,12:{},4:45,5:234}
for x,y in a.items():
    if(y != {}):
        di.update([xy])
print(di)

























