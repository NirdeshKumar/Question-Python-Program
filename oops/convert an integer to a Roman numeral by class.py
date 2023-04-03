

# 1. Write a Python class to convert an integer to a Roman numeral.

class roman:
    def roman_number(self,num):
        value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbol=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        sym=''
        x=0
        while(num>0):
            div=num//value[x]
            num=num%value[x]
            while(div):
                sym=sym+symbol[x]
                div=div-1
            x=x+1
        return sym
obj=roman()
num=int(input("enter a number : "))
print(roman().roman_number(num))
print(obj.roman_number(num))
