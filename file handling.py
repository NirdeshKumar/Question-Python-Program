
'''
                                                                                                             
r-----
only read file if your file name exist in your system             

a----
you can only append(write) in file name either file exist or niether exist  
(does not remove previous data), you can not read the data on run time
            
w-----
you can only append(write) in file name either file exist or niether exist  
(it remove previous data), you can not read the data on run time
            
x-----
only create a file if your file name does not exist in your system          


    MODE                   READ           WRITE          CREATE        REMOVE PREVIOUS DATA                                           

--- r ----                (YES)          (NO)            (NO)            (NO)

--- a ----                (NO)           (YES)           (YES)           (NO)

--- w ----                (NO)           (YES)           (YES)           (YES)
            
--- x ----                (NO)           (NO)            (YES)            ---


# ADVANCED MODE           READ           WRITE          CREATE        REMOVE PREVIOUS DATA

--- r+ ----              (YES)          (YES)           (NO)          (NO)

--- a+ ----              (YES)          (YES)           (YES)        (NO)

--- w+ ----              (YES)          (YES)           (YES)        (YES)

--- x+ ----              (YES)          (NO)            (YES)        (NO)

'''


# FILE CREATE AND WRITE

f=open("basic.txt","w")
f.write("this is my first file which is create by you.\n")
f.close()

m=open("basic.txt","r")
print(m.read())

# REMOVE FILE IF EXIST

import os
os.remove("basic.txt")

# READ FILE IF FILE EXIST IN SYSTEM

f = open("D:\Advance.python\program.py", "r")
print(f.read(12)

# FILE CREATE AND WRITE
      
f=open("basic.txt","w")
f.write("this is my first file which is create by you.\n")
f.close()

# FILE READ
      
m=open("basic.txt","r")
print(m.read())

# REMOVE FILE IF EXIST
      
import os
os.remove("basic.txt")

# FILE READ SOME WORDS 

f = open("D:\Advance.python\program.py", "r")
print(f.read(12))

# READLINE() FUNCTION 

file=open("basic.txt","r")
#file.write("this is siddharth singh")
#file.seek(0)
print(file.readline())
print(file.readline())
file.close()

# Open a File on the Server

file=open("basic.txt")
print(file.read())

# Return the 15 first characters of the file:
file=open("basic.txt")
print(file.read(5))

# Read one line of the file

file=open("basic.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()


# Loop through the file line by line

#file=open("basic.txt","r")
for x in file:
    print(x)


file=open("basic.txt","r")
file.write("Open the file demofile2.txt and append content to the file:")
file.close()

print(file.read())


import os
os,remove("basic.txt")


import os
if os.path.exists("basic.txt"):
    os.remove("basic.txt")
else:
    print("file does not exist!!!!")



file=open("basic.txt","r")
#file.write("this is siddharth singh")
#file.seek(0)
print(file.readline())
print(file.readline())
file.close()

# Open a File on the Server

file=open("basic.txt")
print(file.read())

# Return the 15 first characters of the file:
file=open("basic.txt")
print(file.read(5))

# Read one line of the file

file=open("basic.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

# Loop through the file line by line

#file=open("basic.txt","r")
for x in file:
    print(x)

file=open("basic.txt","r")
file.write("Open the file demofile2.txt and append content to the file:")
file.close()

print(file.read())

import os
os,remove("basic.txt")

# FILE REMOVE IF FILE EXIST IF FILE NOT EXIST THEN GIVE NOT FOUND FILE

import os
if os.path.exists("basic.txt"):
    os.remove("basic.txt")
else:
    print("file does not exist!!!!")
