
# Method overloading by dispatch

from multipledispatch import dispatch 
class calculation :
    @dispatch(int,int,int)
    def add(self,a,b,c=0):
        print("Addition",a+b+c)
    @dispatch(str,str,str)
    def add(self,a,b,c=''):
        print("Subtractioon",(a+c)+b)
    @dispatch(str,str,int)
    def add(self,a,b,c=1):
        print("addition",(a+b)*c)

obj=calculation()
obj.add(1,32,4)
obj.add("nir","sh","de")
obj.add("nir","sh",12)
