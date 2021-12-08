#Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else
#print ‘COMMON YEAR’
Year = int(input("Enter the Year: "))  
if ((Year%400==0) or (Year%100!=0 and Year%4==0)):
    print("Entered year is leap year.")
else:
    print("Entered year is not a leep year.")