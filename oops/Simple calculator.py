
# Simple calculator

class calculation :
    
    def add(self,a,b,c=0):
        print("Addition",a+b+c)

    def sub(self,a,b,c=0):
        print("Subtractioon",(a+c)-b)

    def multi(self,a,b,c=1):
        print("Multipication",a*b*c)

    def div(self,a,b,c=1):
        print("Division",(a+b)/c)

obj=calculation()
obj.add(1,32,4)
obj.sub(1,22,4)
obj.multi(1,2,4)
obj.div(1,12)
obj.multi(11,2,4)
