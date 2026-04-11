# Script: Simulates a simple store interaction (item, price, quantity).
# Notes/Lessons Learned:
# - Using f-strings to print values and totals
# - Using type casting to manipulate user input for calculations
# - Utilizing new-lines for output formatting

print("Welcome to the shop!")
item = input("What item are you looking for? ")
price = float(input(f"What is the price of {item}? "))
quantity = float(input(f"How many of {item} are you purchasing? "))

print(f"Added {quantity} {item}(s) to shopping cart \n Subtotal: ${price * quantity}")
