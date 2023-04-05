
# Private Attribute

class A:
    def __init__(self):
        self.name="Nirdesh"
        self.add="Noida"
        self.__age=21
        self.__sal=1000000
        print(self.name,"\n",self.add)
        
    def private(self):
        print(f"{self.__age}\n{self.__sal}")
obj=A()

