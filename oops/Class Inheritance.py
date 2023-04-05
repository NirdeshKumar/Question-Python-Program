



# Class Inheritance

class college():
    coll="TMU University"
    def __init__(self,na,a,id,add):
        self.name=na
        self.age=a
        self.stu_id=id
        self.address=add
    def detail(self):
        "Students Details"
        print(f"Name:- {self.name}\nAge:- {self.age}\nStudent_ID:- {self.stu_id}\nAddress:- {self.address}")

class student(college):
    pass
obj=student("Siddharth Singh",21,"TCA1920065","Noida")
print(obj.detail.__doc__)
print("College Name:- ",obj.coll)
obj.detail()
