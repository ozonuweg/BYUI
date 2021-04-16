"""
File: prove12.py
Prove: 12
Topic: Spanish Flu Dataset
Author: Glory Ozonuwe

Purpose: Write a program to help analyze the large amount of data.
"""
high = 0
country_high = ""
year_high = ""

low = 9999999999
country_low = ""
year_low = ""

search_high = 0
search_country_high = ""

search_low = 999999999
search_country_low = ""

total = 0
average = 0
count = 0

print()
print("This program contains a Dataset from an article on the Spanish Flu that comes from OurWorldinData.org")
print("It has been automated to enable the easy access to information about various countries life expectancy from 1543 to 2019.")
print("Feel Free to type in a year you want to know more about.")
print()
# search_year = int(input("Type in a year you want to research on: "))

with open("life-expectancy.csv") as life_expectancy_file:
    next(life_expectancy_file)

    for line in life_expectancy_file:
        parts = line.split(",")

        entity = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        # # Print data for the year the user searches for
        # if search_year == year:
        #     count += 1
        #     total += life_expectancy
        #     average = total / count

        #     # Find highest value for the year searched
        #     if life_expectancy > search_high:
        #         search_high = life_expectancy
        #         search_country_high = entity

        #     # Find lowest value for the year searched
        #     if life_expectancy < search_low:
        #         search_low = life_expectancy
        #         search_country_low = entity
            

        # Find Highest Life Expectancy with year and country for Dataset
        if life_expectancy > high:
            high = life_expectancy
            country_high = entity
            year_high = year
        
        # Find Lowest Life Expectancy with year and country for Dataset
        if life_expectancy < low:
            low = life_expectancy
            country_low = entity
            year_low = year
    
    # print(f"The average life expectancy in {search_year} was {average:.2f}")
    # print(f"The country with the lowest life expectancy in {search_year} was {search_country_low} with {search_low:.2f}")
    # print(f"The country with the highest life expectancy in {search_year} was {search_country_high} with {search_high:.2f}")
    print()
    print(f"The country with the lowest life expectancy in the dataset was {country_low} in {year_low} with {low:.2f}")
    print(f"The country with the highest life expectancy in the dataset was {country_high} in {year_high} with {high:.2f}")
    print()
    print("Bye! Thank you.")
    print()