
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& PROGRAM &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#divmod(dividend, divisor)
'''
n=int(input())
m=int(input())
x=divmod(n,m)
print(x)
'''

# WAP take a list by user and find the sum sort reverse etc.
'''
num = int(input("how many value enter in list : "))
list=[]
for i in range(num):
    val=int(input("enter value : "))
    list.append(val)
print(list)
print(sum(list))
print(max(list))
print(min(list))
list.sort()
print(list)
list.reverse()
print(list)
#list.count()
#print(list)

#adding new value

list.append(53)
print(list)

list.extend([22,443,12,435,66])
print(list)

list.insert(3,78)
print(list)

#Replace

list.pop()
print(list)

list.pop(3)
print(list)

list.remove(6)
print(list)

list.clear()
print(list)

new=list.copy()
print(index(53))


del list
print(list)
print(new)


'''

# WAP to add only integer value in a list
'''
num=int(input("How many value enter in list : "))
list=[]
add=0
for i in range(num):
    val=eval(input("enter value: "))
    list.append(val)
for y in list:
    if(type(y)==int or type(y)==float):
        add +=y
print(add)        
'''

# WAP to count how many element of bool, string, float, complex and integer.
'''
num=int(input("how many value enter in list: "))
list=[]
count=0
count2=0
count3=0
count4=0
count5=0
for i in range(num):
    val=eval(input("enter a value: "))
    list.append(val)
for x in list:
    if(type(x)==int):
        count += 1
    
    elif(type(x)==str):
        count2 += 1    
    
    elif(type(x)==bool):
        count3 += 1
    
    elif(type(x)==complex):
        count4 += 1
    
    elif(type(x)==float):
        count5 += 1
print(f'int {count}\nstring {count2}\nbooling {count3}\ncomplex {count4}\nfloat {count5}')

'''

# WAP to add list element and insert in new list
'''
num=int(input("How many value enter in list : "))
list=[]
list1=[]
add=0
list3=[]
for i in range(num):
    val=eval(input("enter value: "))
    list.append(val)


num=int(input("How many value enter in list : "))
for i in range(num):
    val=eval(input("enter value: "))
    list1.append(val)


print(list)
print(list1)

if (list<list1):
    for x in range(len(list)):
        add=list[x]+list1[x]
        list3.append(add)
    print(list3)        
else:
    for y in range(len(list1)):
        add=list[y]+list1[y]
        list3.append(add)
    print(list3)                   

'''

# WAP to print a number 1 to 51 by list comprehension
'''
num=[x for x in range(1,52)]
print(num)

# odd number

num=[x for x in range(1,55,2)]
print(num)

#sum of even number

num= [x for x in range (2,99,2)]
print(num)
print(sum(num))

# prime number

'''

# *******************WHILE PROGRAM****************************

# WAP to print a table by using while loop
'''
num=int(input("enter a table value : "))
x=1`
while(x<=10):
    print(f' {num} * {x} = ', num*x)
    x +=1
'''


# WAP to print a sum of natural number
'''
num=int(input("enter a value to Natural Number : "))
x=1
su=0
while(x<=num):
    su +=x    
    x +=1
    
print(su)    
 
'''

# WAP to find a factorial number
'''
num=int(input("enter a value : "))
fact=1
x=1
while(x<=num):
    fact = fact*x
    x +=1
print(fact)    
'''

# WAP to print prime number

#num=int(input("enter a value : "))

'''
x=1
c=[]
while(x<=100):
    i=2
    count=0    
    while(i<x):
    #for i in range(2,x):
        if (x%i==0):
            count +=1
        i += 1
    if(count==0):
        print(x)
        c.append(x)
      
    x += 1
print(sum(c))

'''
    
# Write a program in Python to reverse a word.

'''
a=input("enter a word: ")
new=''
for i in a:
    new=i+new
    
print(new)

#                or

a=input("enter a value: ")
print(a[::-1])
'''

# Write a program to print n natural number in descending order using a while loop.

'''
x=1
c=[]
a = int(input("enter value: "))
for i in range(1,a+1):
    c.append(i)
c.reverse()
print(c)

#                     or


x=1
c=[]
a = int(input("enter value: "))
while(x<=a):
    c.append(x)
    x +=1
c.reverse()
print(c)

'''


# WAP to separate positive and negative number from a list.

''' 
q=[]
x=0
c=[]
d=[]
a=int(input("enter a value: "))
for i in range(a):
    val=int(input("enter a value: "))
    q.append(val)

while(x<len(q)):
    if(q[x]>=0):                                          
        c.append(q[x])
    else:
        d.append(q[x])
    x += 1
print(c)
print(d)
   
'''

# ***************************** TUPLE ********************************

# 1. VIEW---(Same as a list)

'''
a= (12,23,43,(33,55,76,21,(98,9,54,(65,49),89),53,89),23,32)
print(type(a))
s=a[3][4][3][0]
print(s)

print(a[3][4][3][1])

#print(a.index([33,55,76,21,[98,9,54,[65,49],89],53,89]))

print(list(enumerate(a)))
'''
'''
n = (12,23,43,33,55,76,21,98,9,54,65,49,89,53,89,23,32)

print(n[1:])
print(n[2:16])
print(n[7:-9])
print(n[4::-1])
print(n[12::2])
print(n[1:-3:2])
print(n[4:-4:2])
print(n[-3:4:2])
print(n[1:9:-2])
print(n[-2:-9:-2])
print(n[-9::-2])
print(n[-1:-12:1])
'''
'''
print(sum(n))
print(max(n))
print(min(n))
print(n.count(89))
print(n.index(65))
'''
# 2.INSERT--- (not possible)
# 3.UPDATE--- (not possible)
# 4.DELETE--- (only del is possible)


# ***************************************************** SET ************************************************

# 1.VIEW----(not possible eg. a[2][3][0])
'''
se={}
print(type(se))
a=set()
print(type(a))
'''
#a={12,12,34,54,2,121,23,543,234,342}
#print(a)

# 2.INSERT----(add(only single value),update(for multiplr value))
'''
a=set()
a.add(98)
print(a)
a.update([12,34,56,78,89,43,65,678,65,89])
print(a)
print(sorted(a))
'''
# 3.DELETE-----(pop(),remove(),discard(),clear(),del)
               #a.pop(2)-------(does not support due to indexing)   
'''
print(a)
a.pop()

print(a)
a.remove(89)
print(a)
#a.remove(89)
#print(a)           
a.discard(89)
print(a)
a.clear()
print(a)
del a
print(a)


'''
# **************************************** ADDITIONAL FEATURE OF SET ********************************************

'''
a=set()
b=set()
a.add(98)
#print(a)
a.update([12,34,56,78])
#print(a)

b.add(1)
b.update([2,3,4,56,78,8])

print(a|b)
print(a.union(b))

print(a.intersection(b))
print(a&b)

print(a.difference(b))
print(a-b)

print(b.difference(a))
print(b-a)

print(a.symmetric_difference(b))
print(a^b)
'''

# WAP to convert a list of characters into a string.
'''
lis=['a','d','s','f']
new=''
for i in lis:
    new=new+i
print(new)    
'''
# Write a Python program to find the second smallest number in a list.
'''    
a=[12,454,5,55,32,23,7,8,786,678]
s=min(a)
a.remove(s)
print(min(a))
'''
#*********************** or *******************************
'''
a=[12,454,5,55,32,23,2,8,786,678]
li=0
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if(a[j]>a[j+1]):
            li=a[j]
            a[j]=a[j+1]
            a[j+1]=li           
print(a[1])        
'''

# Write a Python program to find the smallest number in a list.

'''
a=[12,23,2,234,54,65,22,1,6,87,9]

small=a[0]
for i in a:
    if(small<i):
        small=i
    if(s_max<i and s_max!=small):
print(small)
'''

# Write a Python program to find the largest number in a list.
'''

a=[12,23,2,234,54,65,22,1,6,875,9]
large=a[0]
for i in a:
    if(large<i):
        large=i
print(large)        
'''

# Write a Python program to find the average in a list.
'''
a=[12,23,2,234,54,65,22,1,6,875,9]
summ=0
count=0
for x in a:
    summ += x
    count +=1
print('avg: ',summ/count)

'''

'''
import random
a=[12,354,5,556,56,34]
random.shuffle(a)
print(a)
'''

#************************************ DICTIONARY ******************************************

# 1. VIEW--- (only view by key)

'''
a={'name':'nirdesh kumar ', 'class':'B.tech','age':21}
print(a['name'])


for x in a:
    print(x,a[x])
'''

# 2. ADDING---(a[key]=value, update() )

'''
a['location']='Moradabad'
a['name']='Ritu Morya'
print(a)

a.update({'age':19,'fees':34000})
print(a)

'''
# ***************************** STRING ******************************************************
'''
a= input("enter name: ").split()
for i in a:
    for j in range(len(i)):
        if(j==0 or j==len(i)-1):
            print(i[j].upper(),end="") 
        else:
            print(i[j].lower(),end="")
'''
'''
lis = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
#lis=[20, 20, 30, 40, 30,50,60]
b=[]


for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if(lis[i]==lis[j]):
            b.append(lis[j])
print(list(set(b)))
'''
'''
a='Rani kumari'
new=''
for x in a:
    if(x!='i'):
        new=new+x
print(new)
'''

# WAP to make a shuffle string

'''
lst = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
flatlist = []
for sublist in lst:
   for item in sublist:
      flatlist.append(item)
print (flatlist)
'''  

# ***************************** Built function of string *****************************


# 1. Converts the first character to upper case

'''
#a=input("enter a string : ")
a='india is a land that represents the blending of beliefs diversities and cultural celebrations we call festivals.'

print("first character is upper case: ",a.capitalize())
print("\n")

# 2. Converts string into lower case
print("string into lower case: ",a.casefold())
print("\n")

# 3. Returns a centered string
print("centered string: ",a.center(34))
print("\n")

# 4. Returns the number of times a specified value occurs in a string
x=input("specific character to count : ")
print("total times a specified value present in a string: ",a.count(x))
print("\n")

# 5. Returns true if the string ends with the specified value
x=input("check that string ends with the specified value or not : ")
print("string ends: ",a.endswith(x))
print("\n")

# 6. Searches the string for a specified value and returns the position of where it was found
x=input("string is present or not in this string : ")
print(a.find(x))
print("\n")

# 7. Returns True if all characters in the string are alphanumeric
print("all characters in the string are alphanumeric: ",a.isalnum())
print("\n")

# 8. Returns True if all characters in the string are in the alphabet
print("all characters in the string are in the alphabet: ",a.isalpha())
print("\n")

# 9. Returns True if all characters in the string are decimals
print("all characters in the string are decimals: ",a.isdecimal()) 
print("\n")

# 10. Returns True if all characters in the string are digits
print("all characters in the string are digits: ",a.isdigit())
print("\n")

# 11. Returns True if all characters in the string are lower case
x=a.lower()  #-------------- Converts a string into lower case
print(x)
print("string are lower case: ",x.islower())
print("\n")

# 12. Returns True if all characters in the string are upper case
x=a.upper()  #-------------- Converts a string into upper case
print(x)
print("string are upper case",x.isupper())
print("\n")

try:
    
# 13. Returns a string where a specified value is replaced with a specified value
    oldvalue=input("enter a old string to replace :")
    newvalue=input("enter a new string: ")
    print(a.replace("value is replaced with a specified value: ",oldvalue, 'newvalue'))#-------------- string.replace(oldvalue, newvalue, count)
    print("\n")
    
    # 16. Returns true if the string starts with the specified value
    x=input("check string start this character or not: ")
    print("tring start this character or not: ",a.startwith(x))
    print("\n")
except:
    print("check your code")

finally:
    

    # 14. Searches the string for a specified value and returns the last position of where it was found
    txt = "Hello, welcome to my world."
    x = txt.rfind("e")
    print(x)
    print("\n")

    # 15. Splits the string at the specified separator, and returns a list
    print("Splits the string: ",a.split())
    print("\n")

    #    17. Swaps cases, lower case becomes upper case and vice versa
    print("lower case becomes upper case: ",a.swapcase())

'''
#-------------------------------------------
'''
class rangeerror(Exception):
    pass
try:
    a=int(input("enter range : "))
    for i in range(a):
        if (a<10):
            raise rangeerror
        else:
            print(i)

except rangeerror:
    print("give you atleast 11 range!!!!")
'''
'''
f=open("basic.txt","w")
f.write("this is my first file which is create by you.\n")
f.close()

m=open("basic.txt","r")
print(m.read())

import os
os.remove("basic.txt")


f = open("D:\Advance.python\program.py", "r")
print(f.read(12))
'''

file=open("basic.txt","r")
#file.write("this is siddharth singh")
#file.seek(0)
print(file.readline())
print(file.readline())
file.close()

# Open a File on the Server
'''
file=open("basic.txt")
print(file.read())

# Return the 15 first characters of the file:
file=open("basic.txt")
print(file.read(5))

# Read one line of the file
'''
'''
file=open("basic.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
'''
'''
# Loop through the file line by line

#file=open("basic.txt","r")
for x in file:
    print(x)
'''
'''
file=open("basic.txt","r")
file.write("Open the file demofile2.txt and append content to the file:")
file.close()

print(file.read())
'''
'''
import os
os,remove("basic.txt")
'''
'''
import os
if os.path.exists("basic.txt"):
    os.remove("basic.txt")
else:
    print("file does not exist!!!!")
'''









































































