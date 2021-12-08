#WAP which accepts marks of four subjects and display total marks,
# percentage and grade. Hint: more than 70% –> 
#distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
a=int(input("enter marks of math: "))
b=int(input("enter marks of science:"))
c=int(input("enter marks of nepali:")) 
d=int(input("enter marks of maths:"))
total_marks=a+b+c+d
print(f"total marks of all subject{total_marks}")
percentage=total_marks/4
print(f"percentage {percentage}")
if percentage>70:
    print("distinction")
elif percentage>60:
    print("first division")
elif  percentage>40:  
    print("pass")
else:
    print("fail")          