# Second script, will accept a string input and detect if the word is a palindrome, matching first/last characters, or is just a normal word.
# Key Takeaways: Using indexes and slices to manipulate and compare text, and using lower() to convert a string to lower-case


string1 = input("Input a string: ")

if len(string1) == 0:
    print("Empty string, try again.")
elif string1.lower() == string1[::-1].lower():
    print("Mirror word")
elif string1[0] == string1[-1]:
    print("Starts and ends same")
else:
    print("Not special")
