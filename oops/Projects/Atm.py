

#  *************************** ATM *********************************

class Atm():
    def __init__(self):
        self.pin=""
        self.balance=0

        self.menu()

    def menu(self):
        print("\n1. Create Pin\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit()")
        user=int(input("Hi, Please Choose Your Option "))

        if(user==1):
            self.create()

        elif(user==2):
            self.deposit()

        elif(user==3):
            self.withdraw()

        elif(user==4):
            self.check()

        elif(user==5):
            exit()

    def create(self):
        self.pin=input("enter a pin: ")
        print("Pin set successfully")


    def deposit(self):
        temp=input("Enter a pin: ")
        if(self.pin==temp):
            bal=int(input("enter deposit amount: "))
            self.balance=self.balance+bal
            print("Depisit successfully")

        else:
            print("invalid pin")

    def withdraw(self):
        temp=input("enter your pin: ")
        if(self.pin==temp):
            bal=int(input("enter amount: "))
            if(self.balance>bal):
                print("withdraw successfully")
            else:
                print("not fund")
        else:
            print("invalid pin")

    def check(self):
        temp=input("enter your pin: ")
        if (temp==self.pin):
            print(self.balance)
        else:
            print("invalid pin")




            











    
        

            
