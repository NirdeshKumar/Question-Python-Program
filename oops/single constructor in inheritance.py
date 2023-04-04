
# single constructor in inheritance


class father:
    def __init__(self,n,a,c):
        self.name=n
        self.age=a
        self.car=c
class son(father):
    pass
obj=son("nirdesh",21,"BMW")
#obj1=son()
print(obj.__dict__)
