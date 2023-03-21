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











