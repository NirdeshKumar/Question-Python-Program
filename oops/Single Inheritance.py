
# Single Inheritance

class father:
    def __init__(self,n,a,c):
        self.name=n
        self.age=a
        self.car=c
class son(father):
    h="yes"
    def dis(self):
        print(self.name,self.age,self.car,son.h)
obj=son("nirdesh",21,"BMW")
obj.dis()
