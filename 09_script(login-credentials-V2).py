# Script: Login Credentials v2
#         Like a previous script, this one simulates an authentication system
#         with username validation, expanded password checks, and a lockout
#         system. (new) This program implements functions to separate validation
#         logic from authentication logic, and utilizes loops to manage repeated
#         attempts.
# Notes/Lessons Learned:
# - Validates username format before authentication
# - Checks if username exists in the system
# - Verifies password against stored credentials
# - Tracks failed login attempts
# - Locks user out after exceeding the attempt limit
# - Grants access on successful login
# - Improved previous version (Script 6) by making the logic 
#   more structured and reusable
# - Huge takeaway was understanding return values and how 
#   those values can be applied to if conditions (ie, true/false)

stored_password = "EXAMPLE1234!"
stored_user = "log"
count = 0

# Password Match Function
def password_check(input_password, stored_password):
    return input_password == stored_password

# Input Validation Function
def username_validation(username):
    if len(username) < 1:
        return False
    elif username.count(" ") > 0:
        return False
    elif not username.isalnum():
        return False
    else:
        return True

# Username/Password Inputs + Checks for Matches (calls password + username function before continuing)  
while True:
    username = input("Username:\n").strip().lower()
    if username_validation(username):
        if username == stored_user:
            input_password = input("Password:\n")
            if password_check(input_password, stored_password):
                print(f"You are now logged in as {username}")
                break
            else: 
                print("Password is incorrect.")
                count += 1
        else:
            count += 1
            print("There is no registered user with that username.")

        if count >= 3:
            print("Attempt Limit Exceeded. Wait 15 minutes before trying to log-in.")
            break
    else:
        print("Username is invalid.")

