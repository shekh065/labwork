'''N students take K apples and distribute them among each other evenly. The remaining
(the indivisible) part remains in the basket. How many apples will each single student
get? How many apples will remain in the basket? The program reads the numbers N and
K. It should print the two answers for the questions above.'''

noof_students = int(input("number of students getting apple"))
noof_apple = int(input("number of apple remaining in basket"))

print( noof_apple // noof_students )
print( noof_apple % noof_students )