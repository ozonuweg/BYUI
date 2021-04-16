"""
File: prove02.py
Prove: 02
Topic: MadLib - Word Games
Author: Glory Ozonuwe

Purpose: Asks user for a series of words and then displays the story with the user's 
words inserted into the appropriate places. 
"""
print()
print("Welcome to Madlib Word Game.")
print("This is a game that displays a story based on series of words you input.")
print()
print("Please enter the following:")
print()
adjective = input("adjective: ")
animal = input("animal: ")
verb = input("verb: ")
exclamation = input("exclamation: ")
adverb = input("adverb: ")
verb1 = input("verb: ")
verb2 = input("verb: ")

print()
print("Your story is:")
print()
print('The other day, I was really in trouble. It all started when I saw a very ' + adjective
+ ' ' + animal + ' ' + verb + ' down the hallway. "' + exclamation.capitalize() + 
'!" I yelled. But all I could think to do was to ' + adverb + ' ' + verb1 + 
' over and over. Miraculously, that caused it to stop, but not before it tried to ' + verb2
+ ' right in front of my family.')
print()
print("Run this program to play again!")
print()


"""
The grading category for this Prove Assignment is >> 5 - Made it your own.
I added additional statements above the story displayed on the screen for this assignment.
I also included an input question "adverb" in the story.
Finally, I closed the story with an invitation to play again.
"""