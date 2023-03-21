

# Write a Python function that accepts a string and counts the number of upper and lower case letters.


def count(n):
    c=0
    ci=0
    s=0
    for i in n:
        if(i.isupper()):
            c += 1
        elif(i.islower()):
            ci += 1
        else:
            s +=1
    print("No. of Upper case characters {}\nNo. of lower case characters {}\nNo. of space {}".format(c,ci,s))
n=input("enetr a sentence: ")
count(n)
