


class student():
    def __init__(self):
        self.name=input("enter a name: ")
        self.age=int(input("enter a age: "))
        self.clas=input("enter a class: ")
        self.sub1="maths"
        self.sub2="english"
        self.sub3="hindi"
        self.sub4="science"
        self.sub5="general knowlegde"
        self.sub6="art"
        
    def sub_det(self):
        print(f"Total Subjects:-\n{self.sub1}\n{self.sub2}\n{self.sub3}\n{self.sub4}\n{self.sub5}\n{self.sub6}")
    def stu_det(self):
        print(f"Name:- {self.name}\nAge:- {self.age} \nClass:- {self.clas}")

class teacher(student):
    def __init__(self):
        self.math_teacher="Nirdesh Kumar"
        self.english_teacher="Shivansh Sharma"
        self.hindi_teacher="Anshika Gupta"
        self.science_teacher="Garima singh"
        self.art_teacher="Siddharth Singh"
        self.general_k_teacher="Abhishek "
        super().__init__()

    def math_teacher(self):
        print(f"Subject Name:- {self.sub1}\nTeacher Name:-\n{self.math_teacher}")
    def english_teacher(self):
        print(f"Subject Name:- {self.sub2}\nTeacher Name:-\n{self.english_teacher}")

    def hindi_teacher(self):
        print(f"Subject Name:- {self.sub3}\nTeacher Name:-\n{self.hindi_teacher}")
    def gk_teacher(self):
        print(f"Subject Name:- {self.sub5}\nTeacher Name:-\n{self.general_k_teacher}")

    def science_teacher(self):
        print(f"Subject Name:- {self.sub4}\nTeacher Name:-\n{self.science_teacher}")

    def art_teacher(self):
        print(f"Subject Name:- {self.sub6}\nTeacher Name:-\n{self.art_teacher}")


    def marks(self):
        if(self.name[0].lower()=="a" or self.name[0].lower()=="s" or self.name[0].lower()=="n" or self.name[0].lower()=="r" or self.name[0].lower()=="p"):
            print(f'Marks Details: \n{self.sub1}: 97\n{self.sub2}: 94\n{self.sub3}: 93\n{self.sub4}: 89\n{self.sub5}: 88\n{self.sub6}: 98\n')
        
        else:
            print(f'Marks Details: \n{self.sub1}: 26\n{self.sub2}: 44\n{self.sub3}: 22\n{self.sub4}: 59\n{self.sub5}: 62\n{self.sub6}: 78\n')

    def attend(self):
        if(self.name[0].lower()=="a" or self.name[0].lower()=="s" or self.name[0].lower()=="n" or self.name[0].lower()=="r" or self.name[0].lower()=="p"):
            print('Attendence Details:\n Very good')
        
        else:
            print('Attendence Details:\n Average good')

class headmaster(teacher):
    
    def teach_attend(self):
        user=input("enter subject name: ")
        if (user.lower()=="math"):
            print('Attendence Details:\n Average good')
        elif (user.lower()=="english"):
            print('Attendence Details:\n good')
        elif (user.lower()=="hindi"):
            print('Attendence Details:\n Very good')
        elif (user.lower()=="science"):
            print('Attendence Details:\n Average good')
        elif (user.lower()=="art"):
            print('Attendence Details:\n good')
        elif (user.lower()=="gk"):
            print('Attendence Details:\n Very good')

    def fess(self):
        if(self.name[0].lower()=="a" or self.name[0].lower()=="s" or self.name[0].lower()=="n" or self.name[0].lower()=="r" or self.name[0].lower()=="p"):
            print(f'Fees Details: \nNot Submitted')
        
        else:
            print(f'Fees Details: \nSubmitted')
    def result(self):
        user=input("enter subject name: ")
        if (user.lower()=="math"):
            print('Result Details:\n Average good')
        elif (user.lower()=="english"):
            print('Result Details:\n good')
        elif (user.lower()=="hindi"):
            print('Result Details:\n Very good')
        elif (user.lower()=="science"):
            print('Result Details:\n Average good')
        elif (user.lower()=="art"):
            print('Result Details:\n good')
        elif (user.lower()=="gk"):
            print('Result Details:\n Very good')
        
        

        
        

        





            
