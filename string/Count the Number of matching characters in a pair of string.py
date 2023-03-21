

 
# Count the Number of matching characters in a pair of string


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
