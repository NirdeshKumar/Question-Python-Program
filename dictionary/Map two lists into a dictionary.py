


# Write a Python program to map two lists into a dictionary.

a=['a','b','c','d','e','f','g']
b=['A','B','C','D','E','F','G']
c={}
for i,j in zip(a,b):
    c[j]=i
print(c)
