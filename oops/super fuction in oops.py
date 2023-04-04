
# super fuction in oops

'''
class father:
    def __init__(self):
        self.name="niredesh"
        self.age=43

class son(father):
    def __init__(self):
        self.car="BMW"
        super().__init__()
obj=son()
print(obj.__dict__)

'''
class father:
    def __init__(self,n,a):
        self.name=n
        self.age=a
class son(father):
    def __init__(self,n,a,v):
        super().__init__(n,a)
        self.mob=v
obj=son("dsa",21,"hvc")
print(obj.__dict__)

