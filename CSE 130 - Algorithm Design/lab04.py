"""
File: lab04.py
Lab : 04
Topic: Monopoly
Author: Glory Ozonuwe

Purpose: Write a program to inform the user if he or she is able to build a hotel on Pennsylvania Avenue. 
This program will ask the user several questions and, based on these questions, tell the user whether 
a hotel can be purchased for Pennsylvania and how much it will cost.

What was the hardest part?: The hardest part was me having to start my code over and over again. That was why 
I took so long. Some of the test sceneraios were faulty so it was hard knowing the requirements.

Duration to complete assignment: 8 hours
"""

print()
cost = 0
houses_needed = 0
houses_available = 0
penn_house_count = 0
pac_house_count = 0
nc_house_count = 0
new_value = 0
total_penn = 0

own_properties = input("Do you own all the green properties? (y/n) ").lower()

if own_properties == "n":
    exit("You cannot purchase a hotel until you own all the properties of a given color group.")

if own_properties != "y":
    exit("Invalid input!")

# if player owns all green properties, prompt for questions
penn_ave_rank = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
pac_ave_rank = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) ")) 
nc_ave_rank = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
print()
bank_available_houses = int(input("How many houses are there to purchase? "))
bank_available_hotels = int(input("How many hotels are there to purchase? "))
print()
players_cash = int(input("How much cash do you have to spend? "))
print()


if penn_ave_rank == 5:
    exit("You have a hotel and Pennsylvania Avenue.\nYou cannot purchase a hotel if the property already has one.")

if penn_ave_rank == 5 and pac_ave_rank == 5 and nc_ave_rank == 5:
    exit("Looks like you've got hotels on all properties.\n You're good!")

if bank_available_houses == 0 and bank_available_hotels == 0:
    exit("The bank has no houses or hotels for purchase.")

if players_cash < 200:
    exit("You do not have sufficient funds to make a purchase at this time.")

# Determine how many houses to add to Pennsylvania Avenue
if penn_ave_rank < 4:
    add_to_penn = 4 - penn_ave_rank
    penn_house_count = 1
    houses_needed += add_to_penn

# Determine how many houses to add to PacificAvenue
if pac_ave_rank < 4:
    add_to_pac = 4 - pac_ave_rank
    pac_house_count = 1
    houses_needed += add_to_pac

# Determine how many houses to add to North Carolina Avenue
if nc_ave_rank < 4:
    add_to_nc = 4 - nc_ave_rank
    nc_house_count = 1
    houses_needed += add_to_nc

# If number of houses needed exceeds the total the bank has, exit with a message
if houses_needed > bank_available_houses:
    exit("There are not enough houses available for purchase at this time.")

if houses_needed <= bank_available_houses:
    houses_available = bank_available_houses
    new_value += 1
else:
    houses_available = bank_available_houses

# Swap if Pennsylvania Avenue has 4 houses and the other two properties have an hotel
if penn_ave_rank == 4 and pac_ave_rank == 5:
    exit("Swap Pacific's hotel with Pennsylvania's 4 houses.")
if penn_ave_rank == 4 and nc_ave_rank == 5:
    exit("Swap North Carolina's hotel with Pennsylvania's 4 houses.")

# Compute and display what to add
if pac_house_count == 1 and houses_available > 0:
    print(f"Add {add_to_pac} house(s) to Pacific.")
    cost += add_to_pac * 200
if nc_house_count == 1 and houses_available > 0:
    print(f"Add {add_to_nc} house(s) to North Carolina.")
    cost += add_to_nc * 200
    houses_available -= add_to_nc
if penn_house_count == 1 and houses_available > 0:
    print(f"Add {add_to_penn} house(s) to Pennsylvania.")
    cost += add_to_penn * 200
    houses_available -= add_to_penn
    penn_ave_rank += add_to_penn

# Compute cost
if players_cash >= cost + 200 and penn_ave_rank == 4:
    exit(f"Put 1 hotel on Pennsylvania.\nThis will cost ${cost + 200}.")
elif players_cash < cost + 200 and total_penn == 4:
    exit(f"Put 1 hotel on Pennsylvania.\nThis will cost ${cost + 200}.\nYou do not have sufficient funds.")