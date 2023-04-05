

# Operator Overloading


class siddharth:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return (self.a+other.a,self.b+other.b)
obj=siddharth(2,21)
obj1=siddharth(4,34)
print(obj+obj1)
