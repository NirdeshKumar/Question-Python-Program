
# 1. INSTANCE METHOD

class school:
    def __init__(self):
        self.name="Siddharth Singh"
        self.age=23
        self.stuID="ASD123"
        self.rollno=12
        print(f"Details:-\n\n{self.name}\n{self.age}\n{self.stuID}\n{self.rollno}")
    def set(self,value,val):
        self.age=value
        self.rollno=val
    def get(self):
        return self.age
        return self.rollno
    def show(self):
        print(f"\n\nDetails:-\n\n{self.name}\n{self.age}\n{self.stuID}\n{self.rollno}")
obj=school()
obj.set(45,34)
print(obj.get())
obj.show()
