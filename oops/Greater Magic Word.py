
# Greater Magic Word

class Test:
    def __init__(self,a):
        self.a=a
    def __gt__(self,other):
        return(self.a>other.a)
t1=Test(12)
t2=Test(34)
print(t1>t2)
    
