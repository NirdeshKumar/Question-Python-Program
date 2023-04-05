
# Mutiply Magic Word

class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __gt__(self,other):
        print(self.a*other.a,self.b*other.b)
        return(self.a*other.a>self.b*other.b)
    def __mul__(self,other):
        print(self.a+other.a,self.b+other.b)
        return (self.a+other.a*self.b+other.b)
t1=Test(12,43)
t2=Test(34,12)
print(t1>t2)
print(t1*t2)
    
