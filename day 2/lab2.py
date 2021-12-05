#find BMI of a person where take mass and height as input from the user
#BMI=mass in kg / (height in m)2
m=int(input("input enter the mass in kg:"))
h=int(input("input enter the height in meter:"))
BMI=(m/h*h)
print(f"the BMI value of person is {BMI}")