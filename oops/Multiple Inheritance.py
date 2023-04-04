
# Multiple Inheritance


class A:
    def __init__(self):
        self.stud_id="stru12"

    def A1(self):
        self.name="sadd"
        self.age=32
class B:
    def __init__(self):
        self.stu_id="stu12"

    def B1(self):
        self.add="Noida"

class C(A,B):
    def __init__(self):
        super().__init__()
        self.father="nirdesh"
    def C1(self):
        self.bro="Mahesh"
        print("Hi Bro")
obj=C()
print(obj.__dict__)
