
# Hybrid Inheritance

class A:
    def __init__(self):
        self.Topic="college"
        
class B():
    def __init__(self):
        super().__init__()
        self.head="Teacher"

class C():
    def __init__(self):
        super().__init__()
        self.head2="Student"

class B1(A,B,C):
    def __init__(self):
        super().__init__()
        self.name="shudhanshu"

class B2(B,C):
    def __init__(self):
        super().__init__()
        self.head_master="Abhishek"

class D(B1,B2):
    def __init__(self):
        super().__init__()
        self.name="siddharth"

stu=D()
print(stu.__dict__)
