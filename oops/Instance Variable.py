
# INSTANCE VARIABLE

class test:
    def __init__(self):
        self.name="Nirdesh Kumar"
        self.age=21
        self.file="yes"
    def show(self):
        print(f"{self.name}\n{self.age}\n{self.file}")
t1=test()
t2=test()
print(t1.name)
t2.show()
