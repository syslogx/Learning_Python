# Second script, will accept a string input and detect if the word is a palindrome, matching first/last characters, or is just a normal word.
# Key Takeaways: Using indexes and slices to manipulate and compare text, and using lower() to convert a string to lower-case

user_input = input("Input a string: ")

if len(user_input) == 0:
    print("Empty string, try again.")
elif len(user_input) == 1:
    print("String is single-character, try a longer string.")
elif user_input.lower() == user_input[::-1].lower():
    print("Mirror word")
elif user_input[0].lower() == user_input[-1].lower():
    print("Starts and ends same")
else:
    print("Not special")
