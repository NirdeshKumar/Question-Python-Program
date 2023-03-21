

#Example 3: Python program to check if the given string is a palindrome.

val=input("enter a string: ")
new=''
for i in val:
    new=i+new
if(val==new):
    print("palindrom")
else:
    print("not palindrom")
