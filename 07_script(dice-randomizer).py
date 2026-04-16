# Script: Rolls user number of dice infinite times until q is pressed to quit.
# Notes/Lessons Learned:
# - Using loops to repeat actions until a condition is met
# - Using randint and the random module to randomize results
# - Using nested loops to structure an action

from random import randint

dice = int(input("How many dice do you want to roll?: "))
sides = int(input("How many sides are on each die: "))

while True:
    for die in range(dice):
        print(randint(1,sides))
    reply = input("Roll again? Press q to quit: ")
    if reply == 'q':
            break
