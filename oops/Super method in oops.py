
# Without Super method in oops

class A:
    def __init__(self):
        self.name="Rakesh"
class B(A):
    def __init__(self):
        self.age=32
class C(B):
    def __init__(self):
        self.add="Noida"

obj=C()
print(obj.__dict__)

#Super method in oops
'''

class A:
    def __init__(self):
        self.name="Rakesh"
class B(A):
    def __init__(self):
        super().__init__()
        self.age=32
class C(B):
    def __init__(self):
        super().__init__()
        self.add="Noida"

obj=C()
print(obj.__dict__)

'''



