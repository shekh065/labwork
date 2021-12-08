'''Ask user to enter age, gender ( M or F ) and then using following rules print their place of service.
if employee is female, then she will work only in urban areas.
if employee is a male and age is in between 20 to 40 then he may work in anywhere
if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
And any other input of age should print "ERROR".'''

A= int(input("Enter the First integer: ")) 
B= int(input("Enter the Second integer: "))  
C= int(input("Enter the Third integer: "))  
sum=A+B+C
if A==B or B==C or A==C:
    print(f"The sum is 0.")
else:
    print(f"the sum is {sum}")