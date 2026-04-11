# Script: Analyzes a string to determine if it is a palindrome,
#         starts and ends with the same character, or neither.
# Notes/Lessons Learned:
# - Using slices and indexes for string comparison
# - Applying lower() for case-insensitive matching
# - Will reject cases of zero/one character inputs

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
