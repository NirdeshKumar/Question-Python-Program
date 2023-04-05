

# Method Overridding

class Test:
    def hindi(self,a):
        self.a=a
        print("Test Hindi Mark: ",self.a)
    def english(self,a):
        self.a=a
        print("Test English Mark: ",self.a)

    def math(self,a):
        self.a=a
        print("Test Math Mark: ",self.a)

    def science(self,a):
        self.a=a
        print("Test Science Mark: ",self.a)

class Test2(Test):
    
    def hindi(self,a):
        self.a=a
        print("Test2 Hindi Mark: ",self.a)
    def english(self,a):
        self.a=a
        print("Test2 English Mark: ",self.a)

    def math(self,a):
        self.a=a
        print("Test2 Math Mark: ",self.a)

    def science(self,a):
        self.a=a
        print("Test2 Science Mark: ",self.a)
    
class Test3(Test2):
    
    def hindi(self,a):
        self.a=a
        print("Test3 Hindi Mark: ",self.a)
    def english(self,a):
        self.a=a
        print("Test3 English Mark: ",self.a)

    def math(self,a):
        self.a=a
        print("Test3 Math Mark: ",self.a)

    def science(self,a):
        self.a=a
        print("Test3 Science Mark: ",self.a)

def call(obj):
    obj.hindi(93)
    obj.english(77)
    obj.math(98)
    obj.science(79)
    print("\n")

T3=Test3()
T2=Test2()
T=Test()
print("**************** Call by function ********************")
call(T3)
call(T2)
call(T)

print("**************** By for loop ********************")


for obj in T3,T2,T:
    obj.hindi(93)
    obj.english(77)
    obj.math(98)
    obj.science(79)
    print("\n")
