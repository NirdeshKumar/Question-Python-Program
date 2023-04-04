

class Rentel:
    def __init__(self):
        self.name="Hero Bike"
        self.name_car="Nano Car"
        self.total_car=21
        self.total=329
        self.menu()

    def menu(self):
        user=int(input("** WELCOME TO BIKE REENTEL AND BUY SYSTEM **\n\n1. Buy a Vhicle \n2. Vhicle on Rent \n3. exit\n"))
        if(user==1):
            inp=int(input("1. Buy a Bike \n2. Buy a Car \ngo out side then press any key :- "))
            if(inp==1):
                
                self.buy_bike()
            elif(inp==2):
                self.buy_car()
            else:
                exit()
            
        elif(user==2):
            inp=int(input("1. Rent a Bike \n2. Car on rent\ngo out side then press any key  :- "))
            if(inp==1):
                self.rent_bike()
            elif(inp==2):
                self.rent_car()
            else:
                exit()
            
        elif(user==3):
            exit()

    
class Bike(Rentel):

    
    def buy_bike(self):
        print("80000 Rs/Bike")
        user=input("if you want buy a bike, press yes: ")
        if(user.lower()=="yes"):
            print(f"Bike Name: {self.name}\nTotal Bikes Available: {self.total}")
            use=int(input("how much buy a bike!!!"))
            if(use<self.total):
                temp=use*80000
                print("Your Payment: ",temp)
                print("Congrates Buddy")
                print(" \n\t\t\t.....ENJOY YOUR DAY.....")
            else:
                print("Sorry Not So Many Bike In This Time\n")
                print("Available bikes:- ",self.total)
        else:
            print("Tanks To Visit My Website!!!")
            
    def rent_bike(self):
        print("Rent:- 400rs/bike\n")
        user=input("if you want rent a bile, press yes: ")
        if(user.lower()=="yes"):
            print(f"Bike Name: {self.name}\nTotal Bikes Available: {self.total}")
            ren=int(input("how much bike take on rent: "))
            if(ren<self.total):
                temp=ren*400
                self.total=self.total-ren
                print("Your Payment:-",temp)
                print("Congrates Buddy! \n\t\t\t.....ENJOY YOUR DAY.....")
            else:
                print("Sorry Not So Many Bike In This Time\n")
                print("Available bikes:- ",self.total)
        else:
            print("Tanks To Visit My Website!!!")


class Car(Bike):
    def buy_car(self):
        print("280000 Rs/Car")
        user=input("if you want buy a Car, press yes: ")
        if(user.lower()=="yes"):
            print(f"Car Name: {self.name_car}\nTotal Cars Available: {self.total_car}")
            use=int(input("how much buy a Car!!!"))
            if(use<self.total_car):
                temp=use*280000
                print("Your Payment: ",temp)
                print("Congrates Buddy")
                print(" \n\t\t\t.....ENJOY YOUR DAY.....")
            else:
                print("Sorry Not So Many Cars In This Time\n")
                print("Available Car:- ",self.total_car)
        else:
            print("Tanks To Visit My Website!!!")
            
    def rent_car(self):
        print("Rent:- 600rs/Car\n")
        user=input("if you want rent a Car, press yes: ")
        if(user.lower()=="yes"):
            print(f"Car Name: {self.name_car}\nTotal Car Available: {self.total_car}")
            ren=int(input("how much Cars take on rent: "))
            if(ren<self.total_car):
                temp=ren*600
                self.total_car=self.total_car-ren
                print("Your Payment:-",temp)
                print("Congrates Buddy! \n\t\t\t.....ENJOY YOUR DAY.....")
            else:
                print("Sorry Not So Many Cars In This Time\n")
                print("Available bikes:- ",self.total_car)
        else:
            print("Tanks To Visit My Website!!!")
    












                       
