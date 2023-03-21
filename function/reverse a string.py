

# Write a Python program to reverse a string.


def rev(a):
    new=''
    for i in a:
        new=i+new
    print(new)

a=input("enter a string: ")
rev(a)
