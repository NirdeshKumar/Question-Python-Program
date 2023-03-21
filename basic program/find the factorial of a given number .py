

# Example 10: Python program to convert the month name to a number of days.


i= int(input("Enter a month date: "))
if(i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12):
    print("31 days in ",i," month.")
elif(i==2):
    year=int(input("enter a year: "))
    if(year%4==0 & year%100 != 0 or year%400==0):
        print("29 days in ",i," month.")
        
    else:
        print("28 days in ",i," month.")
        
else:
    print("30 days in ",i," month.")
  
