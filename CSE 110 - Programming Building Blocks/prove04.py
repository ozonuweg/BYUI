"""
File: prove04.py
Prove: 04
Topic: Meal Price Calculator
Author: Glory Ozonuwe

Purpose: To calculate the price of a meal. 
"""
print()
print("Welcome to Meal Price Calculator Self Service!")

print()
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
num_of_children = int(input("How many children are there? "))
num_of_adult = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate? "))

print()
subtotal = float((child_meal_price * num_of_children) + (adult_meal_price * num_of_adult))
sales_tax = float(subtotal * (sales_tax_rate / 100))
total = float(subtotal + sales_tax)

print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")

print()
payment_amount = float(input("What is the payment amount? "))
tip = float(input("How much tip would you like to give? "))

change = float(payment_amount - total - tip)
print(f"Change: ${change:.2f}")
print()

print("Thank you for using our Self Service Calculator!")
print()