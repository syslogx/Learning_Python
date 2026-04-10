# Third script: Will simulate a store interaction, by asking the user for their item, 
#               the price of that item, and how many they want to purchase
# Key Takeaways: Using f-strings to call variables or perform calculations in the same string, 
#                and using type casting to change inputs to float/int for calculations.

print("Welcome to the shop!")
item = input("What item are you looking for? ")
price = input(f"What is the price of {item}? ")
quantity = input(f"How many of {item} are you purchasing? ")

print(f"Added {quantity} {item}(s) to shopping cart \n Subtotal: ${float(price) * float(quantity)}")
