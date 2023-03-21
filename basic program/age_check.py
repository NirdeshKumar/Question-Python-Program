#*********************************Age Check***********************************

ram=int(input("enter ram age : "))
rani=int(input("enter rani age : "))
moni=int(input("enter moni age : "))
if (ram>rani and ram>moni):
 print("Ram")
elif(rani>moni):
 print("Rani")
else:
 print("moni")