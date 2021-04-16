"""
File: lab02.py
Lab : 02
Topic: Authentication
Author: Glory Ozonuwe

Purpose: Write a program to read the contents of the file into a list. The program will then prompt the 
user for a username and password. Finally, we will tell the user whether the user is authenticated.

What was the hardest part?: The hardest past was me using for loops to compare the username and password lists.
It didn't work and gav me a hard time. It kept on printing for all the indexes. I ended up using try-except 
and just comparing the basic index.There was no difficulty with the instructions or any part of the problem 
definition.

Duration to complete assignment: 4 hours
"""
import json 

# Create empty lists
usernames = []
passwords = []

# Open and run file
with open("Lab02.json") as lab2_file:
    data = json.load(lab2_file)

    # Get lines in username and add to usernames list
    for line in data['username']:
        usernames.append(line)

    # Get lines in password and add to passwords list   
    for line in data['password']:
        passwords.append(line)


print()
# Get username and password from user
get_username = input("Username: ")
get_password = input("Password: ")  

username_index = ""
password_index = ""

try:
    username_index = usernames.index(get_username)
    password_index = passwords.index(get_password)
except:
    username_index = "Black Knight"
    password_index = "Bring out your dead!"

# Using input from user and comparing indexes, print if the user is aunthenticated or not
if username_index != "Black Knight" and password_index != "Bring out your dead!":
    if username_index == password_index:
        print("You are authenticated!")
    else:
        print("You are not authorized to use the system.")
else:
    print("You are not authorized to use the system.")

print()