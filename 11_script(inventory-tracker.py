inventory = {}
history = []
options = ["1", "2", "3", "4", "5"]

def user_action(choice):
    if choice == "1":
        if not inventory:
           print("Inventory is empty.")
        else:
            for k,v in sorted(inventory.items()):
                print(f"{k} (x{v})")
    elif choice == "2":
        added_items = input("What items do you wish to add? ").strip().lower()
        quantity = int(input("How many of that item are you adding? "))
        if added_items in inventory:
            inventory[added_items] += quantity
            history.append(f"You updated {added_items} by {quantity}")
        else:
            inventory[added_items] = quantity
            history.append(f"You added {quantity} {added_items}")
    elif choice == "3": 
        remove_items = input("What item do you wish to remove? ").strip().lower()
        if remove_items in inventory:
            inventory.pop(remove_items)
            history.append(f"You removed {remove_items}")
        else:
            print("You do not have that item in inventory.")
    elif choice == "4":
        used_item = input("What item do you wish to use? ").strip().lower()
        quantity = int(input("How many of that item are you using? "))
        if used_item in inventory:
            if quantity > inventory[used_item]:
                print("You don't have that many.")
            elif quantity == inventory[used_item]:
                del inventory[used_item]
                history.append(f"You used all of your {used_item}s")
            else:
                inventory[used_item] -= quantity
                history.append(f"You used {quantity} {used_item}")
        else: 
            print("You do not have that item to use.")

while True:
    print("1) View Inventory\n2) Add Item\n3) Remove Item\n4) Use Item\n5) Quit")
    choice = input("> ")
    if choice == "5":
        for action in history:
            print(f"- {action}")
        break
    if choice not in options:
        print("That is not a valid choice.")
    else:
        history.append(f"You chose {choice}")
        user_action(choice)
