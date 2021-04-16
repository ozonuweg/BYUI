"""
File: prove13.py
Prove: 13
Topic: Wind Chill Calculations
Author: Glory Ozonuwe

Purpose: Write a program that asks the user for a temperature and then shows the wind chill 
values for various wind speeds at that temperature.
"""

print()
fahrenheit = 0

# Function that computes squares
def compute_windchill(fahrenheit, i):
    # This function computes a windchill and returns it
    # It needs: fahrenheit (temperature) -- and i (windspeed)
    # It returns: the result -- the windchill
    result = 35.74 + (0.6215 * fahrenheit) - (35.75 * (i ** 0.16)) + (0.4275 * fahrenheit * (i ** 0.16))
    return result

# Warm Welcome
print("Welcome to Glory's windchill calculator!")

# Gets temperature and degree type from user
temperature = int(input("What is the temperature? "))
f_or_c = input("Fahrenheit or Celsius (F/C)? ")
f_or_c = f_or_c.upper()

# Compute temperature based on degree type
if f_or_c == "F":
    fahrenheit = temperature
elif f_or_c == "C":
    fahrenheit = (temperature * 9 / 5) + 32

# loop through the windspeed mph from 5-60, counting in 5's
for i in range(5, 61, 5):
    # Call the function to compute the windchill, save the result into a variable
    windchill = compute_windchill(fahrenheit, i)
    # Print the result variable
    print(f"At temperature {fahrenheit:.1f}F, and wind speed {i} mph, the windchill is: {windchill:.2f}F")

print("Thank you, bye!!!")
print()