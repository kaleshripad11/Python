#!/usr/bin/python3
"""
Task - 1
Write a program that prints out the results of at least one calculation for each of 
the basic operations: addition, subtraction, multiplication, division, and exponents.
"""
print("ADDITION       : ",(4+5))
print("SUBTRACTION    : ",(7-4))
print("MULTIPLICATION : ",(8*9))
print("DIVISION       : ",(9/3))
print("POWER          : ",(3**9))
print("----------------------------------------------------------------------------------------------")

"""
Task - 2
Find a calculation whose result depends on the order of operations.
Print the result of this calculation using the standard order of operations.
Use parentheses to force a nonstandard order of operations. Print the result of this calculation.
"""
print(7+3*4/6-1)
print((7+3)*4/6-1)
print("----------------------------------------------------------------------------------------------")

"""
Task - 3
On paper, 0.1+0.2=0.3. But you have seen that in Python, 0.1+0.2=0.30000000000000004.
Find at least one other calculation that results in a long decimal like this.
"""
print(0.7+0.1)
print("----------------------------------------------------------------------------------------------")

# Taks - 4: Use integer division to show whether your Python interpeter is using Python 2 or Python 3
# print 5/2 <===== It is python2 syntax for print statement, and it will print int value which is 2
print(5/2)