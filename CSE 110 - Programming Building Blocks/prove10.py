"""
File: prove10.py
Prove: 10
Topic: Shopping Cart 
Author: Glory Ozonuwe

Purpose: Create a program that stores a list of products in a shopping cart along with their prices,
add item(s), remove items(s), view cart, and compute total price of items in cart.
"""
print()
print("Welcome to the Shopping Cart Program!")

items = []
prices = []

choice = ""
while choice != "5":
    # Display Shopping Cart Menu
    print()
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    choice = input("Please enter an action: ")
    print()

    # Add Item
    if choice == "1":
        add_item = input("What item would you like to add? ")
        items.append(add_item)
        item_price = float(input("What is the price of " + "'" + add_item + "'? " ))
        prices.append(item_price)
        print ("'" + add_item + "' has been added to the cart.")

    # Display/View Cart
    elif choice == "2":
        print("The contents of the shopping cart are:")
        for i in range(len(items)):
            item = items[i]
            price = prices[i]
            print(f"{i+1}. {item:10} -   ${price:.2f}")

    # Remove item from cart
    elif choice == "3":
        index = int(input("Which item would you like to remove? "))
        
        if index - 1 in range(len(items)):
            items.pop(index - 1)
            prices.pop(index - 1)
            print("Item removed.")
        else:
            print("Sorry, that is not a valid item number.")
    
    # Compute Total
    elif choice == "4":
        total = sum(prices)
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

    # Quit
    elif choice == "5":
        print("Thank you. Goodbye.")