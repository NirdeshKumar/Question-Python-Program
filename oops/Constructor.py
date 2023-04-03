
# Constructor

class chetu:
    def __init__(self,n,a,r):#------------------- CONSTRUCTOR
        self.Name=n
        self.Age=a
        self.Rollno=r

    def show(self):
        print(f"details:-\nName:- {self.Name}\nAge:- {self.Age}\nRollno:- {self.Rollno}")


obj=chetu("nirdesh",21,12)
obj.show()
