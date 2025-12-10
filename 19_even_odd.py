# This script accepts two numbers from the user and display even or odd numbers based upon the user preferrence
# 1. Validates the input to ensure both fields are not empty.
# 2. Ensures both values contain only numeric characters (supports negative numbers).

def lines():
    print("*"*100)

# Prompt for user input
first_number = input("Enter the first number: \n")
second_number= input("Enter the second number: \n")

# If user input is empty
if len(first_number) == 0 or len(second_number) == 0:
    if len(first_number) > 0 and len(second_number) == 0:
        lines()
        print("User input --> Second number field is empty")
    elif len(first_number) == 0 and len(second_number) > 0:
        lines()
        print("User input --> First number field is empty")
    elif len(first_number) == 0 and len(second_number) == 0:
        lines()
        print("User input --> First number field is empty")
        print("User input --> Second number field is empty")

# user input is not empty
# Validation -- To make sure the user input contain only numeric values i.e. postive and negative
# Validation check pass -- Display even or odd numbers based upon the user preferrence

elif len(first_number) > 0 and len(second_number) > 0:
    if not first_number.lstrip("-").isdigit() or not second_number.lstrip("-").isdigit():
        if first_number.lstrip("-").isdigit() and not second_number.lstrip("-").isdigit():
            lines()
            print("Second number field must contain only numeric values")
        elif not first_number.lstrip("-").isdigit() and second_number.lstrip("-").isdigit():
            lines()
            print("First number field must contain only numeric values")
        elif not first_number.lstrip("-").isdigit() and not second_number.lstrip("-").isdigit():
            lines()
            print("First number field must contain only numeric values")
            print("Second number field must contain only numeric values")

    elif first_number.lstrip("-").isdigit() and second_number.lstrip("-").isdigit():
        first_number = int(first_number)
        second_number = int(second_number)

        if first_number == second_number:
            lines()
            print(f"First number: {first_number} is equal to Second number: {second_number}")

        elif first_number > second_number:
            lines()
            print(f"First number: {first_number} is greater than Second number: {second_number}")

        elif first_number < second_number:
            lines()
            choice = input("Would you like to print even or odd numbers:\n")
            choice = choice.lower()

            if choice == "even":
                for even_numbers in range(first_number, second_number +1):
                    if even_numbers%2==0:
                        print(f"Even number --> {even_numbers}")

            elif choice == "odd":
                for odd_numbers in range(first_number, second_number + 1):
                    if odd_numbers % 2 != 0:
                        print(f"Odd number --> {odd_numbers}")

            else:
                lines()
                print("Invalid user input")

