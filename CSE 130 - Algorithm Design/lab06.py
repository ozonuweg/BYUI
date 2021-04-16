"""
File: lab06.py
Lab : 06
Topic: Advanced Search Program
Author: Glory Ozonuwe

Purpose: It prompt the user for a filename. We will then read the contents of the file into a list. The 
program will then prompt the user for a name. Finally, we will tell the user whether the name is in the list.

Algorithmic Efficiency: Logarithmic Performance O(log n) Doubling the size of the input should slow execution 
by 1 time unit.
There is a Loop controlled by the input in some way. Every iteration of the loop must cut the size of the input 
by a fraction. In almost all cases, that fraction is a half resulting in a log2 n equation. If the loop cuts
the size by a third, then the resulting algorithm is still logarithmic but the equation is log3 n.

What was the hardest part?: The hardest part figuring out the encoding because of the special characters in
some country names. The countries-file didn't run until I used the latin encoding.

Duration to complete assignment: 2 hours
"""

import json
import os
file_list = []

# Get file name from user
print()
file_name = input("What is the name of the file? ")

# Open and run file with latin encoding for special characters. Exit if file not found.
try:
    with open(file_name, encoding = "ISO-8859-1") as lab6_file:
        data = json.load(lab6_file)

        for line in data['array']:
            file_list.append(line)
except IOError:
    exit("File not found.\n")

# Get the search word from user
word = input("What name are we looking for? ")

# Check and output if file is empty
if os.stat(file_name).st_size == 0:
    exit("The file is empty.\n")
elif not file_list:
    exit("The file is empty.\n")

# Function that performs the advanced search
def advanced_Search(file_list, word):
    start = 0
    end = len(file_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if file_list[mid] == word:
            return f"We found {word} in {file_name}."
        elif word < file_list[mid]:
            end = mid - 1
        else:               
            start = mid + 1
    
    return f"{word} not found in {file_name}."

# Output the result of search
print (advanced_Search(file_list, word))
print()