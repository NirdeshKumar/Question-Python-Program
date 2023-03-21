

# Python program to capitalize the first and last character of each word in a string


a=input("enter a name: ").split()
for i in a:
    for x in range(len(i)):
        if(x==0 or x==len(i)-1):
            print(i[x].upper(),end='')
        else:
            print(i[x].lower(),end='')
    print(end=' ')
