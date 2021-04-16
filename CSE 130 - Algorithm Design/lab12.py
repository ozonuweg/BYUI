"""
File: lab12.py
Lab : 12
Topic: Prime Number Program
Author: Glory Ozonuwe

Purpose: This program will display all the prime numbers at or below a certain value. It will first 
prompt the user for an integer. If the integer is less than 2, then the program will prompt the user 
for another number. The program will then compute all the prime numbers below (and including) the 
given number. When finished, the program will display the list of prime numbers.

What was the hardest part?: There wasn't anything particularly hard. The pseudocode I
made last week helped as usual. Comparing mine with the instructor's own made the process smooth.

Duration to complete assignment: 1 hour 
"""
# Import math library
import math

# Get number from user
number = input("\nThis program will find all the prime numbers at or below N. Select that N: ")

# Assertion Error for string, decimal, non-integer input
assert number.lstrip('-').isdigit(), "User input is not valid. Number must be a positive integer >= 2!\n"

number = int(number)
# Repeat till number greater than 1
while number <= 1:
    number = int(input("ERROR! Can only compute prime numbers at or below N if N is >= 2! Select that N: "))

# Initialize & declare array
prime = []

# Add all the numbers between 2 and user-inputed number to the array
for i in range(2, number + 1):
    prime.append(i)

# Check that the length of the array matches the expected number based on input, N
assert len(prime) == number  - 1

# Sort prime numbers from prime array
factor = 2

while factor <= int(math.sqrt(number)):
    # Check if factor is in the prime array
    if factor in prime:
        # Check for multiples of the factor
        for multiple in range(factor * 2, number + 1, factor):
            # Delete multiples from prime array if found
            if multiple in prime:
                prime.remove(multiple)
    # Increment to next factor
    factor += 1
    assert factor >= 2

# Output final prime list
if len(prime) == 1:
    print(f"The prime number at or below {number} is {prime}\n")
else:
    print(f"The prime numbers at or below {number} are {prime}\n")
