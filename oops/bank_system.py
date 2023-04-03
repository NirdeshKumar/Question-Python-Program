
class user():
    def __init__(self):
        self.name=input("enter your name: ")
        self.age=int(input("enter your Age: "))
        self.sex=input("enter your Sex: ")
        self.pin=""
        self.amount=0

    def show_det(self):
        print(f"*******ACCOUNT DETAILS *********\nName:- {self.name}\nAge:- {self.age}\nsex:- {self.sex}\nBalance:- {self.amount}")
class Bank(user):

    def create_pin(self):
        self.pin=input("enter a pin: ")

    def deposit(self):
        inp=input("enter a pin: ")
        if (inp==self.pin):
            user=int(input("enter a amount: "))
            self.amount=self.amount+user
            print("Total Amount: ",self.amount)
        else:
            print("Invalid Pin")

    def withdraw(self):
        inp=input("enter a pin: ")
        if (inp==self.pin):
            user=int(input("enter a amount: "))
            if(user<self.amount):
                self.amount=self.amount-user
                print("withdraw successful!!!")
            else:
                print("Insuffucient Balance\nAvailable Balance:-   ",self.amount)
        else:
            print("Invalid Pin")
    def check(self):
        inp=input("Enter a pin: ")
        if(self.pin==inp):
            print("Total Amount: ",self.amount)
        else:
            print("invalid pin")
    
