# usr/bin/python3
"""ABS_7_strongPasswordDetection.py - detects whether a given password is strong or not
A strong password is defined as one that is at least eight characters long,
contains both uppercase and lowercase characters, and has at least one digit."""

import re, pyperclip

# Strong password regexes
passLengthRegex = re.compile(r'.{8,}')  # contains 8 or more characters
passUpperRegex = re.compile(r'[A-Z]')   # contains an uppercase letter
passLowerRegex = re.compile(r'[a-z]')   # contains a lowercase letter
passDigitRegex = re.compile(r'\d')      # contains a digit 

# Function to check the regexes
def pass_strength_checker(text):
    if passLengthRegex.search(text) == None:     #earlier version from GitHub was 'if passLengthRegex is None'- this was wrong
        return False
    if passUpperRegex.search(text) == None:
        return False
    if passLowerRegex.search(text) == None:
        return False
    if passDigitRegex.search(text) == None:
        return False
    else:
        return True

# Get password from the clipboard
password = str(pyperclip.paste())
print(password)

# Run password through function and print relevant message to console
if pass_strength_checker(password) == True:
    print("Your password is strong.")
else:
    print('''Try again. A strong password must be least eight characters long,
contain both uppercase and lowercase characters,and have at least one digit.''')
