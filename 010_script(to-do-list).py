# Script: Daily To-Do List
#         Functions as a daily checklist, will ask for input (a task)
#         will add it to a list and display the list, and will allow you
#         to check that task off by entering its number. Has a help
#         screen/output, and will run continuously until 'q' is entered.
#         Prints the users completed tasks after 'q' is pressed.

# Notes/Lessons Learned
# - Goal was to practice list manipulation and basic program flow
# - Uses for loops to iterate over lists and display items
# - Utilizes .pop() to remove items from the to-do list by index
# - Utilizes .append() to add new tasks and store completed tasks
# - Uses .isnumeric() to validate numeric input for safe indexing
# - Learned how list indexing connects user input to specific items

header = """
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
                            
"""
print(header)

todos = []
completed = []
while True:
    for task in range(len(todos)):
        print(f"{task+1}) {todos[task]}")
        
    print("***********************************")
    print("Enter a command. Type 'h' for help:")
    command = input("> ")
    if command == "q":
        break
    elif command == "h":
        print("TODO LIST HELP")
        print("Type 'q' to quit")
        print("To add a todo to the list, type it and hit enter")
        print("To complete a todo enter its number")
    elif command.isnumeric():
        idx = int(command) - 1
        if idx >= len(todos):
            print("THERE IS NO TODO WITH THAT NUMBER!")
        else:
            done_todo = todos.pop(idx)
            completed.append(done_todo)
    else: 
        todos.append(command)
    # Print todos from list
if completed:
    print(f"You completed {len(completed)} todos today: ")
    for todo in completed:
        print(f"* {todo}")
