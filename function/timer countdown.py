import time

def count(t):
    while(t):
        mins,sec=divmod(t,60)
        tim="{}:{}".format(mins,sec)
        print(tim)
        time.sleep(1)
        t -=1
    print("timer completed!!!")
t=int(input("enter a time"))
count(t)
        

