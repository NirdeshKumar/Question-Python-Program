

# 1. Converts the first character to upper case


#a=input("enter a string : ")
a='india is a land that represents the blending of beliefs diversities and cultural celebrations we call festivals.'

print("first character is upper case: ",a.capitalize())
print("\n")

# 2. Converts string into lower case
print("string into lower case: ",a.casefold())
print("\n")

# 3. Returns a centered string
print("centered string: ",a.center(34))
print("\n")

# 4. Returns the number of times a specified value occurs in a string
x=input("specific character to count : ")
print("total times a specified value present in a string: ",a.count(x))
print("\n")

# 5. Returns true if the string ends with the specified value
x=input("check that string ends with the specified value or not : ")
print("string ends: ",a.endswith(x))
print("\n")

# 6. Searches the string for a specified value and returns the position of where it was found
x=input("string is present or not in this string : ")
print(a.find(x))
print("\n")

# 7. Returns True if all characters in the string are alphanumeric
print("all characters in the string are alphanumeric: ",a.isalnum())
print("\n")

# 8. Returns True if all characters in the string are in the alphabet
print("all characters in the string are in the alphabet: ",a.isalpha())
print("\n")

# 9. Returns True if all characters in the string are decimals
print("all characters in the string are decimals: ",a.isdecimal()) 
print("\n")

# 10. Returns True if all characters in the string are digits
print("all characters in the string are digits: ",a.isdigit())
print("\n")

# 11. Returns True if all characters in the string are lower case
x=a.lower()  #-------------- Converts a string into lower case
print(x)
print("string are lower case: ",x.islower())
print("\n")

# 12. Returns True if all characters in the string are upper case
x=a.upper()  #-------------- Converts a string into upper case
print(x)
print("string are upper case",x.isupper())
print("\n")
