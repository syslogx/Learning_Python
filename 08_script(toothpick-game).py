# Script: Toothpick Game
# Notes/Lessons Learned:
# - While True can be used to simplify loop conditions. 
#   it will run until a break condition stops it
# - Uses nested loops to check parts of the game, 
#   such as active player, toothpick count, etc.

toothpick = 20 
Player_1 = input("What is your name: ") 
Player_2 = input("What is your name: ") 
curr_player = Player_1

# Player Choices
while True:
    print("| " * toothpick) 
    print(f"There are {toothpick} toothpicks left")
    choice = int(input(f"How many toothpicks will {curr_player} take? ")) 
    while choice not in [1, 2 , 3]:
        choice = int(input("You must choose 1, 2, or 3. Choose again: "))
    toothpick -= choice 
    if toothpick <= 0: 
        print(f"{curr_player} WINS!")
        print("Game over!")
        break
    if curr_player == Player_1:
        curr_player = Player_2
    else:
        curr_player = Player_1
    
