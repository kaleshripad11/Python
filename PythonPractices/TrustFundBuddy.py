'''
Created on 18-Jun-2020

@author: shree
'''
# Trust Fund Buddy - Bad
# Demonstrates a logical error
print(
"""
Trust Fund Buddy
Totals your monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).
Please enter the requested, monthly costs.
pennies and use only dollar amounts.
"""
)
car = float(input("Lamborghini Tune-Ups: "))
rent = float(input("Manhattan Apartment: "))
jet = float(input("Private Jet Rental: "))

total = car + rent + jet
print("\nGrand Total:", total)
input("\n\nPress the enter key to exit.")