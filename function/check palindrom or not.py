

# Write a Python program to check a string is palindrom or not.


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
