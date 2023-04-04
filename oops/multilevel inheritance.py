

# multilevel inheritance


class G_father:
    c=98
    def __init__(self):
        self.G_name="siddharth"
        super().__init__()

class father(G_father):
    def __init__(self):
        self.F_name="mohit"
        super().__init__()

class son(father):
    def __init__(self):
        self.name="rajesh"
        super().__init__()
obj=son()
print(obj.__dict__)
print(obj.name)
print(obj.G_name)
print(obj.F_name)

