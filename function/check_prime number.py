


# use of function view(),insert(),


def view():
    a=int(input("enter a index value to acces: "))
    print(n[a])
    
def insert():
    b=int(input("enter a insert value in list: "))
    n.append(b)
    print(n)
    
def in_insert():
    b=int(input("enter index position:"))
    c=int(input("enter value: "))
    n.insert(b,c)
    print(n)
    
def delete():
    c=int(input("enter a delete value in list: "))
    n.remove(c)
    print(n)
    
def v_pop():
    b=int(input("enter index position to remove element:"))
    n.pop(b)
    print(n)
    
n=[]
num=int(input("enter a store limit in list: "))
for i in range(num):
    val=int(input("enter a value: "))
    n.append(val)

    
print("1. If you want to view list, press key 1:\n ")
print("2. If you want to delete particular element in list, press key 2:\n ")
print("3. If you want to insert element in list, press key 3:\n ")
print("4. If you want to insert element at specific position in list, press key 4:\n ")
print("5. If you want to delete element at specific position in list, press key 5:\n ")

x=int(input("choose option: "))


if(x==1):
    view()
if(x==2):
    delete()
if(x==3):
    insert()
if(x==4):
    in_insert()
if(x==5):
    v_pop()
