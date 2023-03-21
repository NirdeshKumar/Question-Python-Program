 #Example 1:

"""
a=[12,34,23,65,45,3,356,45,90]
for i in a:
 print(i)

"""

#Example 2: Python program to count the total number of digits in a number.
"""
val=input("enter a number: ")
#s=str(val)
c=0
for i in val:
    c += 1
    print(c)    
"""

#Example 3: Python program to check if the given string is a palindrome.
'''
val=input("enter a string: ")
new=''
for i in val:
    new=i+new
if(val==new):
    print("palindrom")
else:
    print("not palindrom")
'''
#Example 4: Python program to check if a given number is an Armstrong number

#val=int(input("enter a number: "))
'''
val=input("enter a number: ")
sum=0
p=int(val)
for i in val:
    m=int(i)
    product=m*m*m
    sum = sum+product
print(sum)
if (sum == p):
   print(f"{val} is a armstrong number.")
else:
    print(f"{val} is not armstrong number.")
'''

#Example 5: Python program to count the number of even and odd numbers from a series of numbers.

'''

m=int(input("count loop: "))
for i in range(m):
    val=int(input("enter a number: "))
    count=0
    s=0
    for x in range(2,val+1,2):
        count += 1
    print(count)
    for var in range(1,val+1,2):
        s += 1
    print(s)    

'''

#Example 6: Python program to display all numbers within a range except the prime numbers.
'''

m=int(input("enter limit: "))
for i in range(m):
    num=int(input("enter a value : "))
    for j in range(1,num+1):
        for k in range(2,j):
            if (j%k==0):
                print(j)
                break
            
            
'''
#Example 7: Python program to find the factorial of a given number.

'''
num=int(input("enter a limit loop: "))
for i in range(num):
    val=int(input("enter a number: "))
    fact=1
    for i in range(1,val+1):
        fact *= i
    print(fact)
    
'''


#Example 8: Python program to get the Fibonacci series between 0 to 50 .

'''
num=int(input("enter Limit: "))
for i in range(num):
    val=int(input("enter a number: "))
    sum=0
    for x in range(0,val+1):
        sum = sum+x
        print(sum)
'''
#Example 9: Python program that accepts a string and calculates the number of digits and letters.
'''
num=int(input("loop Limit : "))
for i in range(num):
    val=input("enter a number or string : ")
    count=0
    for x in val:
        count += 1
    print(count)    
'''
# Example 10: Python program to convert the month name to a number of days.
'''
num=int(input("Loop Limit : "))
for x in range(num):
    val= int(input("Enter a value: "))
    
    for i in range(1,13):
        if(i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12):
            print("31 days in ",val," month.")
            break
        elif(i==2):
            year=int(input("enter a year: "))
            if(year%4==0 & year%100 != 0 or year%400==0):
                print("29 days in ",val," month.")
                break
            else:
                print("28 days in ",val," month.")
                break
        else:
            print("30 days in ",val," month.")
            break

'''

#Example 11: **********************Driving License***************
"""
age=int(input("enter your age : "))
if (age>=18 and age<60):
 print("you are eligible. ")
elif(age<18):
 print("sabr kr bsdk ")
else:
 print("bsdk tumari umar nhi hai abhi chalane ki")
"""


#Example 12: ***********************Vowel check***************************
'''

vow=input("enter a alphabates: ")
if(vow=='A' or vow=='E' or vow=='I' or vow=='O' or vow=='U' or vow=='a' or vow=='e' or vow=='i' or vow=='o' or vow=='u'):
 print(f"{vow} is vowel ")
else:
 print(f"{vow} is consonent ")

'''


#Example 13:*********************************Age Check***********************************
'''
ram=int(input("enter ram age : "))
rani=int(input("enter rani age : "))
moni=int(input("enter moni age : "))
if (ram>rani and ram>moni):
 print("Ram")
elif(rani>moni):
 print("Rani")
else:
 print("moni")

#*********************************Age Check 2***********************************

ram=int(input("enter ram age : "))
rani=int(input("enter rani age : "))
moni=int(input("enter moni age : "))

if(ram>rani):
 if(ram>moni):
  print("Ram")
 else:
  print("Moni")
else:
 if(rani>moni):
  print("Rani")
 else:
  print("Moni")

'''

#Example 14:****************************************Calculator***********************************************

'''
num1=int(input("enter a number: "))
num2=int(input("enter 2nd number: "))

print(" 1. Add\n 2. Subtract\n 3. Multiply\n 4. division\n 5. modulus\n 6. Exponential\n 7. exit() ")
val=int(input("Choose your operator : "))

if(val==1):
 print("Adding",num1+num2)

elif(val==2):
 if(num1>num2):
  print("subtract",num1-num2)
 else:
  print("subtract",num2-num1)

elif(val==3):
 print("Multiplication",num1*num2)

elif(val==4):
 if(num2==0 ):
  print("Infinite")
 else:
  print("Division",num1/num2)

elif(val==5):
 print("Modulus",num1%num2)

elif(val==6):
 print("Exponential",num1**num2)

elif(val==7):
 exit()
else:
 print("Invalid Value")

'''

#Example 15:************************************table*************************************

'''
var=int(input("no.:"))
for i in range(1,11):
 print(f"{var} * {i} = ",var*i)
'''


#Example 15:********************************** add natural number*************************
'''
val=int(input("enter a value : "))
sum=0
for i in range(1,val+1):
 sum +=i
 print(sum)
print(sum)
'''

#Example 16:********************************** sum odd number*************************
'''
val=int(input("enter a value : "))
sum=0
for x in range(1,val+1):
 if (x%2!=0):
  sum +=x
  print(sum)
 else:
  pass
print(sum)
''' 

#Example 17:********************************** factorial number*************************
'''
val=int(input("enter a valur: "))
fact=1
for x in range(1,val+1):
 fact *=x
print(fact)
'''

#Example 18:********************************** prime number or not*************************

''' 
val=int(input("enter a value: "))
count=0
for i in range(2,val):
 if (val%i==0):
  count +=1
if (count==0):
 print("prime")
else:
 print("not prime") 
'''

#Example 19:********************************** print prime number*************************
'''
val=int(input("enter a number: "))
for i in range(1,val+1):
 count=0
 for x in range(2,i):
  if (i%x==0):
   count +=1
 if(count==0):
#print("prime number \n")
  print(i)
''' 

#Example 20: Print the first 10 natural numbers using for loop.

'''
for i in range(1,11):
 print(i)
'''

#Example 21: Python program to print all the even numbers within the given range.
'''
val=int(input("enter a value: "))
for i in range(2,val+1,2):
 print(i)

'''
'''
a=[12,2,3,12,14,65]
b=[54,1,54,65,34,89]
d=[]

for i in a:
    for x in b:
        c=i+x
        break
    d.append(c)
print(d)

'''
# Write a Python program to count the number of strings from a given list of strings.The string length is 2 or more and the first and last characters are the same
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2


#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2
'''
a=['abc','ada','rer','122111','343']
count=0
for i in range(len(a)):
    y=a[i]
    if(y[:1]==y[-1:]):
        count += 1
        
print(count)

#        or

a=['abc','ada','rer','122111','343']
count=0
for i in a:
    if(i[0]==i[-1]):
        count += 1
        
print(count)

'''
'''
a=[1,2,3,4,5,3,2,6,7,4]
c=[]
for i in range(len(a)):
    count=0
    print(i)
    for x in a:
        if(a[i]==x):
            count += 1
            print(x)
            break
    if (count==2):
        c.append(x)
print(c)    

    
     
a=[1,2,3,4,5,3,2,6,7,4]
c=[]
for i in a:
    if(i not in c):
        c.append(i)
print(c)


'''
# ********************************** STRING *****************************************************

# Python program to capitalize the first character of each word in a string.

'''
a=input("enter : ").split()
#a=['nirdesh','kumar']
for i in a:
    print(i.capitalize(),end=' ')
    
'''

# Python program to even number character is upper and odd number character is lower of each word in a string.

'''
#a=input()
a='nirdesh kumar'
n=''
for i in range(len(a)):
    if(i%2==0):
        print(a[i].upper(),end='')
    else:
        print(a[i].lower(),end='')
       
   
'''

# Python program to capitalize the first and last character of each word in a string

'''
a=input("enter a name: ").split()
#a="siddharth",'weds','aayushi'
for i in a:
    for x in range(len(i)):
        if(x==0 or x==len(i)-1):
            print(i[x].upper(),end='')
        else:
            print(i[x].lower(),end='')
    print(end=' ')
'''
 
# To print even length words in string
'''
a=input("enter a string: ").split()
for i in a:
    for x in range(len(i)):
        if(x%2==0):
            print(i[x],end='')
    print(end=" ")        
'''

# Ways to remove i’th character from string in Python
'''
a=input()
new=''
for y in a:
    if(y != 'i'):
        new=new+y
print(new)    
'''
#-------------- OR ------------------------------------
'''
a=input("enter the string:").split()
for i in a:
    for j in i:
        if(j!="i"):
            print(j,end="")
'''        
# Count the Number of matching characters in a pair of string

'''
#str2='rajevkumari'
#str1='ikjesah'
str1=input("enter a string: ")
str2=input('enter a other string: ')

count=0
if (len(str1)>len(str2)):
    for i in str2:
        if(i in str1):
            count +=1
    print(count)
    
if (len(str2)>len(str1)):
    for i in str1:
        if(i in str2):
            count +=1
    print(count)
'''
#-------------------------- OR --------------------------------------
'''
str1=input("enter a string: ")
str2=input('enter a other string: ')

count=0
for x,y in zip(str1,str2):
    if(x in str2):
        count +=1
print(count)
    
'''    


# Python Program to remove all duplicates from a given string
'''
#str1='rajeev kummar'
str1=input("enter a string: ")
str2=''
for i in str1:
    if(i not in str2):
        str2=str2+i
print(str2)        
'''
 

# Python | Remove empty tuples from a list

'''
a=[(),[1,2,3],(2,6,8),7,9,89,(),67]

b=[]
for i in a:
    if(i != ()):
        b.append(a[i])
print(b)
'''

# Python | Remove tuples from a list

'''
a=[(),[1,2,3],(2,6,8),7,9,89,(),67]

b=[]
for i in range(len(a)):
    
    if(type(a[i])!=tuple):
        b.append(a[i])
print(b)        
'''

# Python – Convert List to List of dictionaries

'''
a=[1,'asd',34,'eee','rty']
b=[2,4,5,6,7]
new={}
for x,y in zip(a,b):
    new[x]=y
print(new)

'''

# Python | Program to print duplicates from a list of integers

'''
a=[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
b=set()

for i in a:
    count=0
    for j in range(len(a)-1):
        if (i==a[j+1]):
            count +=1
    if(count>1):
        b.update([i])
print(list(b))
'''

# Python – Maximum and Minimum K elements without max function in list

'''
a=[1,2,3,4,65,64,7,38,94,11,22,33,44,55]
b=a[0]
for i in a:
    if(i>b):
        b=i
print(b)        
'''       

# Python –WAP to sorting list without sort function.

'''
a=[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
for i in range(len(a)-1):
    for j in range(0,len(a)-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)
'''
        
# ************************************************ TUPLE **********************************************************

# Python – Maximum and Minimum K elements in Tuple

'''
a=(1,2,3,4,65,64,7,38,94,11,22,33,44,55)
b=a[0]
for i in a:
    if(i>b):
        b=i
print(b)        

'''

# Python | Merging two Dictionaries

'''
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

dict1.update(dict2)
print(dict1)

'''

# ZeroDivisionError

'''
a=int(input("enter value : "))
b=int(input("enter value : "))
try:
    c=a/b
    
except ZeroDivisionError:
    print("you can't give zero value in secound value")
else:
    print(a/b)
'''

# AttributeError

'''
a=12
a.append(4)
print(a)
'''

'''
a=[]
val=int(input("how much value add in list : "))
for i in range(val):
    num=int(input("enter a", [i+1],"value"))
    try:
        if(type(num)==str):
            
    except AttributeError:
        print("you can't give string ")
    else:
        if(type(num)==str):
            continue
            a.append(num)
        
'''

'''
                                                                                             READ           WRITE          CREATE      REMOVE PREVIOUS DATA                                           
r-----------only read file if your file name exist in your system                            (YES)          (NO)            (NO)          (NO)

a-----------you can only append(write) in file name either file exist or niether exist        (NO)         (YES)          (YES)           (NO)
            (does not remove previous data), you can not read the data on run time
            
w-----------you can only append(write) in file name either file exist or niether exist        (NO)          (YES)         (YES)         (YES)
            (it remove previous data), you can not read the data on run time
            
x-----------only create a file if your file name does not exist in your system               (NO)            (NO)         (YES)         ---
'''

# ADVANCED MODE

'''

r+ ---------                                                                                 (YES)         (YES)           (NO)          (NO)

a+ ------------                                                                              (YES)          (YES)           (YES)        (NO)

w+ ------------                                                                               (YES)          (YES)           (YES)        (YES)

x+ --------                                                                                    (YES)          (NO)            (YES)        (NO)

'''

'''
f=open("abc.txt","r+")
f.write("hello, how are you ")
f.tell()
f.seek(0)
print(f.read())
f.close()
'''
'''
print(f.read())
'''















            




















     
    





































































































































    
