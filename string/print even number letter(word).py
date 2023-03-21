

 
# To print even length words in string

a=input("enter a string: ").split()
for i in a:
    for x in range(len(i)):
        if(x%2==0):
            print(i[x],end='')
    print(end=" ")  
