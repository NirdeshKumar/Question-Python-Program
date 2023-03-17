

# How to Print Multiple Arguments in Python?

'''
def multi_arg(name,age,clas,p_name):
    print("your name is {} \n your father name is {} \n your class is {} \n your age is {} ".format(name,p_name,clas,age))


a,b,c,d="nirdesh kumar",21,12,"papa"
multi_arg(a,b,c,d)
'''

# Python program to find the power of a number using recursion

'''
def power(x,y):
    print(x**y)

x=int(input())
y=int(input())
power(x,y)

'''

# Sorting objects of user defined class in Python.

'''
def sorting(n):
    for i in range(len(n)-1):
        for j in range(len(n)-1):
            if(n[j]>n[j+1]):
                temp=n[j]
                n[j]=n[j+1]
                n[j+1]=temp
                
a=int(input("enter a value: "))
b=[]
for y in range(a):
    val=int(input("enter a {} value: ".format(y)))
    b.append(val)
    
sorting(b)
print(b)
'''

# Write a Python function to sum all the numbers in a list.

'''
def add(n):
    count=0
    for j in n:
        count +=j
    print(count)
        
a=int(input("enter a value: "))
b=[]
for y in range(a):
    val=int(input("enter a {} value: ".format(y)))
    b.append(val)

add(b)
'''

# Write a Python program to reverse a string.

'''
def rev(a):
    new=''
    for i in a:
        new=i+new
    print(new)

a=input("enter a string: ")
rev(a)
'''

# Write a Python program to check a string is palindrom or not.

'''
def rev(a):
    new=''
    for i in a:
        new=i+new
    print(new)
    if(new==a):
        print("palindrom")
    else:
        print("not palindrom")

a=input("enter a string: ")
rev(a)
'''

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument

'''
def fact(n):
    facti=1
    if(n<=0):
        print(" {} value not supported".format(a))
    else:
        for i in range(1,n+1):
            facti *= i
        print(facti)

a=int(input("enter a value (zero and negative value not support): "))
fact(a)
'''

# Write a Python function that accepts a string and counts the number of upper and lower case letters.
'''
def count(n):
    c=0
    ci=0
    s=0
    for i in n:
        if(i.isupper()):
            c += 1
        elif(i.islower()):
            ci += 1
        else:
            s +=1
    print("No. of Upper case characters {}\nNo. of lower case characters {}\nNo. of space {}".format(c,ci,s))
n=input("enetr a sentence: ")
count(n)
'''

# Write a Python function that takes a list and returns a new list without duplicate value.

'''
def rem_dup(n):

    b=[]
    for i in n:
        if(i not in b):
            b.append(i)

    print(b)
n=[]
num=int(input("enter a store limit in list: "))
for i in range(num):
    val=int(input("enter a value: "))
    n.append(val)

rem_dup(n)
'''

# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

'''
def check_prime(n):
    c=0
    for i in range(2,n):
        if(n%i==0):
            c += 1   
    if(c==0):
        print("prime number")
    else:
        print("not prime number")

n=int(input("enter a value: "))
check_prime(n

'''

# viwe

def view(a):
    print(n[a])
def insert(b):
    n.append(b)
    print(n)
def delete(c):
    n.remove(c)
    print(n)
    

n=[]
num=int(input("enter a store limit in list: "))
for i in range(num):
    val=int(input("enter a value: "))
    n.append(val)
a=int(input("enter a index value to acces: "))
b=int(input("enter a insert value in list: "))
c=int(input("enter a delete value in list: "))
view(a)
delete(c)
insert(b)

    















