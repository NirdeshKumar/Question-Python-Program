
# multiple constructor inheritance


class father:
    def __init__(self,n,a,c):
        self.name=n
        self.age=a
        self.car=c
        print("dsb")
class son(father):
    def __init__(self,n,a):
        self.name=n
        self.age=a
        
obj=son("nnnn",21)

#obj1=son("nnnn",21,"ssssx") # error - 3 positional arguments but 4 were given

print(obj.__dict__)

#print(obj1.__dict__)
