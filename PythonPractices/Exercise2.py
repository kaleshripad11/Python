#!/usr/bin/python3
"""
Task - 1
Find a quote that you like. Store the quote in a variable, 
with an appropriate introduction such as "Ken Thompson once said, 
'One of my most productive days was throwing away 1000 lines of code'". 
Print the quote.
"""

quote = """Ken Thompson once said, 
'One of my most productive days was throwing away 1000 lines of code'"""

print(quote)
print('-----------------------------------------------------------------------')

"""
Task - 2
Store your first name, in lowercase, in a variable.
Using that one variable, print your name in lowercase, Titlecase, and UPPERCASE.
"""
my_name = "anonymous"
print(my_name)
print(my_name.title())
print(my_name.upper())
print('-----------------------------------------------------------------------')

# Task - 3: Store your first name and last name in separate variables, and then combine them to print out your full name.
f_name = "Onion"
l_name = "Router"
print("Full Name : ",(f_name+" "+l_name))
print('-----------------------------------------------------------------------')

"""
Task - 4
Choose a person you look up to. Store their first and last names in separate variables.
Use concatenation to make a sentence about this person, and store that sentence in a variable.-
Print the sentence.
"""
f_name = 'Iko'
l_name = 'Uwais'
info = f_name+" "+l_name+" "+"is an Thai martial artist and actor!"
print(info)
print('-----------------------------------------------------------------------')

"""
Task - 5
Store your first name in a variable, but include at least two kinds of whitespace on each side of your name.
Print your name as it is stored.
Print your name with whitespace stripped from the left side, then from the right side, then from both sides.
"""
f_name = ' Iko '
print("-"+f_name+"-")
print("-"+f_name.lstrip()+"-")
print("-"+f_name.rstrip()+"-")
print("-"+f_name.strip()+"-")
print('-----------------------------------------------------------------------')
