# This Python script accepts two numbers from the user and prints all numbers
# between them (inclusive), except the number 10. 
# It demonstrates input validation, type checking, and the use of the `continue` statement

def lines():
    print("*"*100)

# Take input from the user
first_number = input("Enter the first number\n")
second_number = input("Enter the second number\n")

# Check if either input is empty
if len(first_number) == 0 or len(second_number) == 0:
    if len(first_number) > 0 and len(second_number) == 0:
        lines()
        print("User input --> Second number field is empty")
    elif len(first_number) == 0 and len(second_number) > 0:
        lines()
        print("User input --> First number field is empty")
    elif len(first_number) == 0 and len(second_number) > 0:
        print("User input --> First number field is empty")
        print("User input --> Second number field is empty")

# User input not empty
# Validation -- make sure the user input contain only numeric values
# Check if both inputs are numeric, convert the value from strings to integers

elif len(first_number) > 0 and len(second_number) > 0:
    if not first_number.isdigit() or not second_number.isdigit():
        if first_number.isdigit() and not second_number.isdigit():
            lines()
            print("Second number field must contain only numeric values")
        elif not first_number.isdigit() and second_number.isdigit():
            lines()
            print("First number field must contain only numeric values")
        elif not first_number.isdigit() and not second_number.isdigit():
            lines()
            print("First number field must contain only numeric values")
            print("Second number field must contain only numeric values")

    elif first_number.isdigit() and second_number.isdigit():
        first_number = int(first_number)
        second_number = int(second_number)

        for numbers in range(first_number, second_number + 1):
            if numbers == 10:
                continue
            else:
                print(f"Number is {numbers}")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This Python script accepts two numeric inputs from the user and prints
# all numbers between them (inclusive). When the loop encounters the 
# number 10, it stops executing further iterations using the `break` statement.
def lines():
    print("*"*100)

# user input
first_number = input("Enter the first number\n")
second_number = input("Enter the second number\n")

# User input -- empty
if len(first_number) == 0 or len(second_number) == 0:
    if len(first_number) > 0 and len(second_number) == 0:
        lines()
        print("User input --> Second number field is empty")
    elif len(first_number) == 0 and len(second_number) > 0:
        lines()
        print("User input --> First number field is empty")
    elif len(first_number) == 0 and len(second_number) > 0:
        print("User input --> First number field is empty")
        print("User input --> Second number field is empty")

# User input not empty
# Validation check -- User input must be numbers only 
# Check if both inputs are numeric, convert the value from strings to integers

elif len(first_number) > 0 and len(second_number) > 0:
    if not first_number.isdigit() or not second_number.isdigit():
        if first_number.isdigit() and not second_number.isdigit():
            lines()
            print("Second number field must contain only numeric values")
        elif not first_number.isdigit() and second_number.isdigit():
            lines()
            print("First number field must contain only numeric values")
        elif not first_number.isdigit() and not second_number.isdigit():
            lines()
            print("First number field must contain only numeric values")
            print("Second number field must contain only numeric values")

    elif first_number.isdigit() and second_number.isdigit():
        first_number = int(first_number)
        second_number = int(second_number)

        for numbers in range(first_number, second_number + 1):
            if numbers == 10:
                break
            else:
                print(f"Number is {numbers}")

