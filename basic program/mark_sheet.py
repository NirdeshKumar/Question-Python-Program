#*****************************Marksheet******************************

name    =  input("enter your Name: ")
roll_no =  int(input("Enter your roll no.: "))

hindi   =  float(input("Hindi Marks : "))
eng     =  float(input("English Marks : "))
maths   =  float(input("Maths Marks : "))
phy     =  float(input("Physics Marks : "))
chem    =  float(input("Chemistry Marks : "))

c=0

list=[hindi,eng,maths,phy,chem]

sum     =  hindi+eng+maths+phy+chem
print("Obtained Mark is: ",sum)

perc   = sum*0.2
print("Percentage is: ",perc)

for i in range(0,len(list)):
 if (list[i]<33):
  c += 1
  
print(c)

if(sum>500 and sum<0)
 print("Check Marks!! ")
 if(hindi==31):
  print("hindi",hindi+2)
 
elif(c=>2):

elif(perc>=91):
 print("Grade: A\n Pass ")
elif(perc>=81):
 print("Grade: B\n Pass ")
elif(perc>=71):
 print("Grade: C\n Pass ")
elif(perc>=61):
 print("Grade: D\n Pass ")
elif(perc>=51):
 print("Grade: E\n Pass ")
elif(perc>=41):
 print("Grade: F\n Pass ")
elif(perc>=33):
 print("Grade: G\n Pass ")

else:
 if (c=>2):
  print("Fail")
 elif() 
 else:

  

