import random

lis=["apple","banana","blueberry","grape","kiwi","mango","orange","pineapple","guava"]
word=random.choice(lis)
dup_word=word

show_list=[]
for i in range(len(dup_word)):
    show_list += "_"
print(show_list)


chance=3
game_over=False
while not game_over:
    print("\n")
    user_g=input("enter a guss value: ").lower()
    for i in range(len(dup_word)):
        letter=dup_word[i]
        if(letter==user_g):
            show_list[i]=user_g
            
    if (user_g not in dup_word):
        chance=chance-1
        print("you have left chance: ",chance)
    if(chance==0):
        game_over=True
        
        print("you lost")
    print(show_list)
    if ("_" not in show_list):
        game_over=True
        print("You WIN Bro......")

print("Original Word: ",dup_word)










        
