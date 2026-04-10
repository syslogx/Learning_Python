# Script: Checks if a three-digit number is even or odd
# Notes/Lessons Learned:
# Alerts the user if the input is not a three-digit number
# Using len() to check digit count, and int() to convert for calculations
# Using if/elif/else to check conditions

number = input("Enter a three digit number: ")
number_length = len(number)

if int(number) % 2 == 0 and number_length == 3:
    print("Your number is even!")
elif number_length == 3 and int(number) % 2 != 0:
    print("Your number is odd.")
else:
    print("You didn't put a three digit number!")


