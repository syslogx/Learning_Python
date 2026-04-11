

txt = input("Please enter a sentence: ").strip().lower()
keyword = input("Please enter your keyword: ").strip().lower()
txt_length = len(txt)


# Prints words and characters from user input
if txt_length == 0:
    print("You did not provide a sentence. Please try again.")
else:
    words = txt.split()
    index = txt.find(keyword)
    print("Analysis Results\n----------------")
    print(f"Words: {len(words)} \nCharacters: {len(txt)}.")

# Prints keyword location from user input
if len(keyword) == 0:
    print("You did not enter a keyword.")
elif index != -1:
    print(f"Keyword found at index {index}.")
else: 
    print("Keyword not found.")
