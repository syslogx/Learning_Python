# Script: Account Login Simulator (Nested Conditionals)
#        Simulates a login system with username validation, password checks,
#        and a warning for bad passwords.
#        Uses structured conditional logic to prioritize security checks
#        (validation → authentication) without using loops.
# Notes/Lessons Learned:
# - Focused on nested conditionals to reinforce authentication
# - Introduces priority-based logic (lockout conditions checked before login)
# - Uses .strip() and .lower() for consistent input normalization
# - Combines validation, warning, and authentication into one example script
# - Trying to learn how to make logic flow efficiently
# - Builds toward real-world concepts like account lockout and access control

username = input("Enter your username: ").strip().lower()
password = input("Enter your password: ").strip()

# Checks for valid username
if len(username) == 0: 
    print("Enter a username")

elif " " in username:
    print("You cannot have spaces in your username")


# Only continue if username is valid
else:
    if "123" in password:
        print("Warning: weak password pattern: ('123') detected")
    
    if username == "admin":
        print("Note: You are logging in as a high-privileged user")
        if len(password) < 8:
            print("Password must be at least 8 characters")
            print("Access Denied.")
        else: 
            print(f"You are now logged in as {username}")
    else:
        if len(password) < 6:
            print("Password must be at least 6 characters")
            print("Access Denied.")
        else:
            print(f"You are now logged in as {username}")
