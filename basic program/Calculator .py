
#Example 14:****************************************Calculator***********************************************




print(" 1. Add\n 2. Subtract\n 3. Multiply\n 4. division\n 5. modulus\n 6. Exponential\n 7. exit() ")
val=int(input("Choose your operator : "))
num1=int(input("enter a number: "))
num2=int(input("enter 2nd number: "))

if(val==1):
 print("Adding",num1+num2)

elif(val==2):
 if(num1>num2):
  print("subtract",num1-num2)
 else:
  print("subtract",num2-num1)

elif(val==3):
 print("Multiplication",num1*num2)

elif(val==4):
 if(num2==0 ):
  print("Infinite")
 else:
  print("Division",num1/num2)

elif(val==5):
 print("Modulus",num1%num2)

elif(val==6):
 print("Exponential",num1**num2)

elif(val==7):
 exit()
else:
 print("Invalid Value")
