#!/usr/bin/python

# Program to create menu/choice based calci
# Get input
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
print("Please select any one from below : \n")
print("1)Addition\n2)Substraction\n3)Division\n4)Multiplication\n5)Power")
ch = int(input("Your choice : "))

# Choice implementation
if ch == 1:
	print("Addition : ",(a+b))
elif ch == 2:
	print("Substraction : ",(a-b))
elif ch == 3:
	print("Division : ",(a/b))
elif ch == 4:
	print("Multiplication : ",(a*b))
elif ch == 5:
	print("Power : ",(a**b))
else:
	print("Please enter the valid choice among the menu!")

