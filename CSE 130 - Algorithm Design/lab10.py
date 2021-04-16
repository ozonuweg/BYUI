"""
File: lab10.py
Lab : 10
Topic: Fibonacci Program
Author: Glory Ozonuwe

Purpose: This program will prompt the user for a positive integer n and then display the nth Fibonacci number.

What was the hardest part?: There wasn't anything particularly hard. The pseudocode I
made last week helped as usual. Comparing mine with the instructor's own made the process smooth.

Duration to complete assignment: 1 hour (YAY! First time.)
"""

# Get number from user
number = input("\nWhich Fibonacci number would you like to see? ")

# Assertion Error for string, decimal, non-integer input
assert number.lstrip('-').isdigit(), "User input is not valid. Number must be a positive integer!\n"

# Make number an integer
number = int(number)

# Dispute negative integer numbers
assert number >= 0, f"Fibonacci {number}. It's a negative number. It must be a poitive integer.\n"

# Set condition if number == 0
if number == 0:
    f0 = 0
    exit(f"Fibonacci number {number} is {f0}\n")

# Declare variables
f1 = 1
f2 = 1
assert f1 >= 1 or f2 >= 1

# Compute fibonacci sequence for numbers >= 2
for i in range(2, number):
    placeholder = f2
    f2 += f1
    f1 = placeholder

# Output fibonacci value
print(f"Fibonacci number {number} is {f2}\n")