"""
File: lab08.py
Lab : 08
Topic: Sort Program
Author: Glory Ozonuwe

Purpose: This program will read a list of names from a file and sort them.

What was the hardest part?: There wasn't anything particularly hard. The pseudocode I
made last week helped a lot. I basically just interpreted the pseudocode. Asserts was
fun to learn and implement. Inserting assert was challenging.

Duration to complete assignment: 2 hours on the dot.
"""

import json
import os
file_list = []

# Get file name from user
print()
file_name = input("What is the name of the file? ")


# Open and run file. Exit if file not found.
assert os.path.isfile(file_name), "Whoops! No such file!\n"

with open(file_name) as lab8_file:
    data = json.load(lab8_file)
    
    for line in data['array']:
        file_list.append(line)


# Check and output if file is empty using assert
assert not os.stat(file_name).st_size == 0, "ERROR! The file is empty.\n"
assert file_list, exit("ERROR! The file is empty.\n")


i_pivot = len(file_list) - 1
i_check = 0
i_largest = 0
assert i_check == 0 and i_largest == 0

# swap function
def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    assert arr[index2] == temp

# sorting conditions
while i_check < i_pivot:
    if file_list[i_check] >= file_list[i_largest]:
        i_largest = i_check

    if i_check == i_pivot - 1:
        if file_list[i_largest] > file_list[i_pivot]:
            swap(file_list, i_largest, i_pivot)
        i_pivot = i_pivot - 1
        i_largest = 0
        i_check = 0
    else:
        i_check = i_check + 1

# print sorted list
assert len(file_list) >= 1, "Looks like there's nothing in the list to print!"
if len(file_list) == 1:
    print(f"The value in {file_name} is:")
    print(*file_list, sep = "\n")
else:
    print(f"The values in {file_name} are:")
    print(*file_list, sep = "\n")
print()