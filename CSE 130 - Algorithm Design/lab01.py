"""
File: lab01.py
Lab : 01
Topic: Guessing Game
Author: Glory Ozonuwe

Purpose: Write a program in Python to display a message on the screen, 
prompt the user for information, make a decision, store data in a list, and loop.

What was the hardest part?: The syntax of python here was annoyiing, but it wasn't the hardest part. 
For me, the aspect of the problem that was difficult to solve was printing the report. I had trouble formatting 
the list to make sure it came out horizontally. I had initially used 
"for guess in numbers:
    print(guess, end" ")"
but that gave me a lot of bugs and problems. I played around with it and found out I could simple use {numbers} and
format it. There was no difficulty with the instructions or any part of the problem definition.

Duration to complete assignment: 2 hours
"""

# Game Introduction
print()
print('This is the "guess a number" game')
print("You try to guess a random number in the smallest number of attempts.")
 
import random

# Ask for Integer
print()
integer = int(input("Pick a positive integer: "))

number = random.randint (1, integer)
numbers = []
guess = 0
count = 0

# User Instructions
print("Guess a number between 1 and " + str(integer) + ".")

# Initialize the sentinal and the array of guesses
while guess != number:
    guess = int(input("> "))
    numbers.append(guess)

    # Play the game and make a decision: 'High', 'Low', 'Guessed it!'
    if guess < number:
        print ("\tToo low!")
    elif guess > number:
        print ("\tToo high!")
    else:
        print ("\tYou guessed it! ")
    count = count + 1

# Give the user a report
print()
print (f"You were able to find the number in {count} guesses.")

print (f"The numbers you guessed were: {numbers}")
print()