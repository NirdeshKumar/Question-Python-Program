
# Hierarchical Inheritance


class A:
    def __init__(self,n,a):
        self.name=n
        self.age=a
        
class B(A):
    def __init__(self,n,a):
        super().__init__(n,a)
        self.roll=12

class C(A):
    def __init__(self,n,a):
        super().__init__(n,a)
        self.roll=22

class B1(B):
    def __init__(self,n,a):
        super().__init__(n,a)
        self.stu_id="stu12"

class B2(B):
    def __init__(self,n,a):
        super().__init__(n,a)
        self.father="rajesh"

class C1(C):
    def __init__(self,n,a):
        super().__init__(n,a)
        self.mother="teena"

class C2(C):
    def __init__(self,n,a):
        super().__init__(n,a)
        self.father="nirdesh"

obj=C2("abhishek",21)
obj1=B2("Adarsh",19)

#print(obj.father)# 'C2' object has no attribute 'father'

print(obj.__dict__)
print(obj1.__dict__)

print(obj.name)
print(obj1.name)

obj.bro="Virendar"
print(obj.__dict__)
