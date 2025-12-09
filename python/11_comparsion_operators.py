# Basic script for COMPARSION operators
# > -- greater than, >= greater than equal to
# < -- less than, <= less than equal to
# == equal to, != not equal to

# Ask the user to enter a password
password = input("Enter the password\n")

# Case 1: User entered nothing
if len(password) == 0:
    print("User Input --> Password field is empty")

# Case 2: Password length is between 1 and 7 characters
elif len(password) <= 7:
    print("Password length is less than or equal to 7")

# Case 3: Password length is 14 or more characters
elif len(password) >= 14:
    print("Excellent")

# Case 4: Password length is between 8 and 13 characters
elif len(password) >= 8 and len(password) < 14:
    print("Password length is greater than or equal to 8")
