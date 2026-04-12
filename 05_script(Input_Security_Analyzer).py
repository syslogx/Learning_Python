# Script: Input Security Analyzer (Rule-Based)
#        Analyzes a user-input username for malicious patterns, suspicious formatting,
#        and basic spam indicators using simple string methods and conditional logic.
#        NOTE! This version is intentionally built without loops, so it uses predefined rules
#        to check for specific dangerous or repetitive patterns.
# Notes/Lessons Learned:
# - Uses strip() and lower() for input normalization
# - Uses in and replace() for detecting and sanitizing malicious patterns
# - Uses count() with threshold rules to simulate basic spam detection
# - Aims for rule-based security filtering (without loops)
# - Has priority handling between malicious and suspicious inputs (mal > sus)
# - Highlights early-stage input validation used in security contexts

username = input("Enter your username: ").strip().lower()
user_length = len(username)
mal = 0
sus = 0
sanname = username

# Checks if username is blank, checks for suspicious input, and for spam
if user_length == 0:
    print("Please provide a username.")
else:
    # Malicious Checks  
    if "select" in username:
        sanname = sanname.replace("select","blocked")
        mal = 1

    if "drop" in username:
        sanname = sanname.replace("drop","blocked")
        mal = 1

    if "delete" in username:
        sanname = sanname.replace("delete", "blocked")
        mal = 1

    if "1=1" in username:
        sanname = sanname.replace('1=1', "blocked")
        mal = 1

    # Suspicious Checks (Limited to "a" or " " as a PoC, as I'm not using loops)
    if username.count(" ") > 5:
        print("Suspicious formatting detected: excessive spaces")
        sanname = sanname.replace(" ", "FLAGGED")
        sus = 1

    if username.count("a") > 5:
        print("Spam detected: Excessive character use")
        sanname = sanname.replace("a", "FLAGGED")
        sus = 1

    # Prints final results
    print("Security Analysis\n*****************")
    print(f"Username: {username}\n")
    
    if mal == 1:
        print("Status: MALICIOUS")
        print("Reason: Contains SQL injection patterns")
        print(f"Sanitized: {sanname}")
   
    elif sus == 1:
        print("Status: SUSPICIOUS")
        print("Reason: Contains spam or suspicious formatting")
        print(f"Sanitized: {sanname}")
   
    else: 
        print("Status: CLEAN")
