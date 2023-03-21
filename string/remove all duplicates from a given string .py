

 

# Python Program to remove all duplicates from a given string

#str1='rajeev kummar'
str1=input("enter a string: ")
str2=''
for i in str1:
    if(i not in str2):
        str2=str2+i
print(str2)  
