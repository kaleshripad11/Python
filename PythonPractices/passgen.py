#!/usr/bin/python3
# This simple python script will generate passwords with max length upto 16

from random import *

# Create 4 strings(for lowercase,for uppercase,for numbers and for symbols)
lower_chars = "abcdefghijklmnopqrstuvwxyz"
upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numerics = "0123456789"
symbolics = "!#$&?"

# Set length for password
length = 16

# Join all the strings
rand_str = lower_chars+upper_chars+numerics+symbolics

# Generate samples using sample() from random class
passwprd = sample(rand_str, length)

# Join the newly generated sequence with join()
password_str = "".join(passwprd)

# Print the password
print("Your randomly generated password is as below : ")
print(password_str)

"""
Output:-
shree@linux:~/Documents/Python2020/BasicExercises$ ./passgen.py 
Your randomly generated password is as below : 
SzkHEj0#&Tq4yPD9
"""
