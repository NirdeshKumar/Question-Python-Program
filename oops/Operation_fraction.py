
class fraction:
    def __init__(self,a,b):
        self.num=a
        self.den=b

    def __str__(self):
        return ("{}/{}".format(self.num,self.den))

    def __add__(self,other):
        self.temp=self.num*other.den+other.num*self.den
        self.temp2=self.den*other.den
        return ("{}/{}".format(self.temp,self.temp2))

    def __sub__(self,other):
        self.temp=self.num*other.den+other.num*self.den
        self.temp2=self.den*other.den
        return ("{}/{}".format(self.temp,self.temp2))
    
    def __mul__(self,other):
        self.temp=(self.num*other.num)
        self.temp2=(self.den*other.den)
        return ("{}/{}".format(self.temp,self.temp2))


