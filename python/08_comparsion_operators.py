# > -- greater than, >= greater than equal to
# < -- less than, <= less than equal to
# == equal to, != not equal to

# Take input for two strings
string_1=input("Enter the first string\n")
string_2=input("Enter the second string\n")

# Function to print a separator line for better output formatting
def lines():
    print("*"*50)

# Check user input, if any empty
if len(string_1) == 0 or len(string_2) == 0:
    if len(string_1) > 0 and len(string_2) == 0:
        lines()
        print("Length of the string 2 is empty")
    if len(string_1) == 0 and len(string_2) > 0:
        lines()
        print("Length of the string 1 is empty")
    elif len(string_1) == 0 and len(string_2) == 0:
        lines()
        print("Length of the string 1 is empty")
        print("Length of the string 2 is empty")

# User input not empty
elif len(string_1) > 0 and len(string_2) > 0:
    if len(string_1) == len(string_2):
        lines()
        print(f"Length of string 1 is {len(string_1)}")
        print(f"Length of string 2 is {len(string_2)}")
        print("Both are equal")

    elif len(string_1) > len(string_2):
        lines()
        print(f"Length of string 1 is {len(string_1)}")
        print(f"Length of string 2 is {len(string_2)}")
        print("Length of the string 1 is greater than string 2")

    elif len(string_1) < len(string_2):
        lines()
        print(f"Length of string 1 is {len(string_1)}")
        print(f"Length of string 2 is {len(string_2)}")
        print("Length of the string 2 is greater than string 1")
