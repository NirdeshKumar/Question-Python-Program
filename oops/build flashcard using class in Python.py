

# Python program to build flashcard using class in Python


import random
class flashcard:
    def __init__(self):
        self.fruits={"apple":"red","orange":"orange","banana":"yellow","rice":"white","grapps":"green"}
    def quiz(self):
            fruit,color=random.choice(list(self.fruits.items()))
            print(f"what is the color of {fruit} ")
            ans=input()
            if(ans.lower()==color):
                print("right answer")
            else:
                print("wrong answer")
            op=int(input("paly again,press 0 "))
            if(op==0):
                obj.quiz()
            else:
                exit()  

obj=flashcard()
obj.quiz()
