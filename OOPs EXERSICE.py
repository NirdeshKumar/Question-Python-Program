

#******************************** OOPs EXERSICE *************************************************

'''
class siddharth:
    money=50000
obj=siddharth()
print(dir(obj))
'''
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

'''
class siddharth:
    money=50000
    
    def Garima(self):
        pass
obj=siddharth()
obj2=siddharth()

obj2.money=20000
obj.sal=100000
siddharth.money=30000
print("obj2",obj2.__dict__)
print(siddharth.money)
print(obj.__dict__)
print(siddharth.__dict__)
'''

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

'''
class match:
    def Run(self):
        print("run run.....")
abhi=match()
siddharth=match()
vansh=match()

print(abhi.Run)
print(match.Run)#---------------give 1 arguments
print(match.Run())
'''

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

'''
class wedding:
    def relation(self,Name,Partner_name,Age):
        self.name=Name
        self.Partner_name=Partner_name
        self.Age=Age

    def show(self):
        print(f"Detail Relationship:-\nName:{self.name}\nPartner Name: {self.Partner_name}\nAge: {self.Age}")

person=wedding()
otherperson=wedding()
chutiya=wedding()

person.relation("siddharth","Garima",21)
otherperson.relation("shivansh","Anshika",21)
chutiya.relation("nirdesh","nagzii",28)
chutiya.show()
person.show()
otherperson.show()
'''

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

'''
a=int(input("enter a value: "))
b=int(input("enter a value: "))
c=int(input("enter a value: "))

class calculator:
    def add(self,a=0,b=0,c=0):
        return(a+b+c)

    def sub(self,a,b=0,c=0):
        return((a+b)-c)
        
    def multi(self,a=1,b=1,c=1):
        print(a*b*c)

obj=calculator()

x=obj.add(a,b,c)
y=obj.sub(x,b,c)
obj.multi(x,y)
print(x,y)

'''

#  Write a Python program to create a class and display the namespace of that class.

'''
class student:
    def name(self):
        pass
obj=student()
print("Display the namespace of that class:- ")
for i in dir(obj):
    print(i)
'''

# Write a Python program to create an instance of a specified class and display the namespace of the said instance.

'''
class shop:
    
    def books(self):
        pass
buyer=shop()

buyer.physics=2
buyer.chemistry=3
buyer.maths=1

print(buyer.__dict__)
'''
   

# Define a Python function student(). Using function attributes display the names of all arguments. 

'''
class school:
    def student(self,n,c,r,b):
        self.sch_name="A.B.C.school"
        self.live="Moradabad"
'''
'''
        self.Name=n    ---------
        self.Class=c            |
        self.Roll_No=r          |--------it declare when these attribute required in other function (pls look above in ffunction)
        self.DOB=b     ---------|
'''        
'''
        print(f"students details:-\nName:- {n}\nClass:- {c}\nRoll No.:- {r}\nDOB:- {b}\nSchool Name:- {self.sch_name}\nlocate:- {self.live}\n\n")
    def student2(self,n,c,r,b):
        
        print(f"students details:-\nName:- {n}\nClass:- {c}\nRoll No.:- {r}\nDOB:- {b}\nSchool Name:- {self.sch_name}\nlocate:- {self.live}")

        

obj=school()

obj.student("siddharth",10,34,"01-feb-2002")
obj.student2("shivansh",9,12,"02-feb-2023")
'''

#  Write a Python function student_data () that will print the ID of a student (student_id). If the user passes an argument student_name or student_class the function will print the student name and class.

'''
class data:
    def student_data(self,s_id,name="",s_class=""):
        print(f"Student ID  {s_id}\nStudent Name  {name}\nStudent class  {s_class}\n\n")
obj=data()
obj.student_data(23,"NIRDESH",14)
'''

#  Write a simple Python class named Student and display its type. Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.

'''
class Student:
    pass

print(Student.__dict__.keys(),"\n")
print(Student.__dict__.values(),"\n")
print(type(Student))
'''

# Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.

'''
class student:
    stu_name="shivansh"
    marks=54
    print(stu_name,"\n",marks)

student.stu_name="siddharth"
student.marks=34
print(student.stu_name)
print(student.marks)
'''
# INSTANCE VARIABLE
'''
class test:
    def __init__(self):
        self.name="Nirdesh Kumar"
        self.age=21
        self.file="Yes"

t1=test()
t2=test()
print(t1.name,t2.name)
'''
'''
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
'''
# CLASS VARIABLE
'''
class school:
    batch="Python"
    batch2="Java"
    def __init__(self):
        self.name="NIrdesh Kumar"
        self.age=21
        self.batch3="c# Language"
t1=school()
t2=school()
t1.batch="C++"
school.batch="C++"
print("\n\n",t1.batch)

print(school.batch)

print("\n",t2.batch)
'''

# TYPES OF METHOD :-
# 1. INSTANCE METHOD
'''
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
        print(f"Details:-\n\n{self.name}\n{self.age}\n{self.stuID}\n{self.rollno}")

obj=school()
obj.set(45,34)
print(obj.get())
obj.show()
'''

# 2. CLASS METHOD

'''
class school:
    batch="python"
    @classmethod
    def stu(cls,value):
        cls.batch=value
        

obj2=school()
obj=school()
obj.stu("Java")
print(obj.batch)
print(school.batch)
print(obj2.batch)

'''

# 3. STATIC METHOD

class school:
    @staticmethod
    def student():
        name="shivansh"
        rollno=12
        print(name,rollno)

obj=school()
obj.student()
school.student()




























































