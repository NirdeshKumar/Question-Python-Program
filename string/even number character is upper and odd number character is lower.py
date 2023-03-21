

# Python program to even number character is upper and odd number character is lower of each word in a string.


#a=input()
a='nirdesh kumar'
n=''
for i in range(len(a)):
    if(i%2==0):
        print(a[i].upper(),end='')
    else:
        print(a[i].lower(),end='')
