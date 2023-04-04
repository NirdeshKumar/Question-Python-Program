#  Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle():
    color="White"
    def __init__(self,n,p,s):
        self.name=n
        self.price=p
        self.speed=s
        print(f"Name: {self.name}\nPrice: {self.price}\nSpeed: {self.speed}")

class bus(Vehicle):
    pass
class car(Vehicle):
    pass

m=car("tata",1000000,120)
print("color:",m.color)
bus("sky",1572000,160)
print("color:",m.color)
