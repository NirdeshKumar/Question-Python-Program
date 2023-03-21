

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument


def fact(n):
    facti=1
    if(n<=0):
        print(" {} value not supported".format(a))
    else:
        for i in range(1,n+1):
            facti *= i
        print(facti)

a=int(input("enter a value (zero and negative value not support): "))
fact(a)
