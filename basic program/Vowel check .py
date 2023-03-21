
#Example 13:*********************************Age Check***********************************

ram=int(input("enter ram age : "))
rani=int(input("enter rani age : "))
moni=int(input("enter moni age : "))
if (ram>rani and ram>moni):
 print("Ram")
elif(rani>moni):
 print("Rani")
else:
 print("moni")


#*********************************Age Check 2***********************************

ram=int(input("enter ram age : "))
rani=int(input("enter rani age : "))
moni=int(input("enter moni age : "))

if(ram>rani):
 if(ram>moni):
  print("Ram")
 else:
  print("Moni")
else:
 if(rani>moni):
  print("Rani")
 else:
  print("Moni")
