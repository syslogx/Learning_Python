# First Python script, simply accepts any three-digit number and checks if it's even or odd. Will alert if the number is more than three digits
# Key Takeaways: Using int() to convert a string to a number for calculations, accepting input, and using if/elif/else to fulfill multiple conditions

number = input("Enter a three digit number: ")
number_length = len(number)

if int(number) % 2 == 0 and number_length == 3:
    print("Your number is even!")
elif number_length == 3 and int(number) % 2 != 0:
    print("Your number is odd.")
else:
    print("You didn't put a three digit number!")


