print("Welcome to the shop!")
item = input("What item are you looking for? ")
price = input(f"What is the price of {item}?")
quantity = input(f"How many of {item} are you purchasing? ")

print(f"Added {quantity} {item}(s) to shopping cart \n Subtotal: ${float(price) * float(quantity)}")