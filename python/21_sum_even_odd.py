# Purpose:
#   - Accept two numbers from the user
#   - Validate empty fields
#   - Validate numeric input (including negative numbers)
#   - Add the numbers and determine whether the sum is even or odd

def lines():
    print("*"*100)

# User input
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
    elif len(first_number) == 0 and len(second_number) == 0:
        lines()
        print("User input --> First number field is empty")
        print("User input --> Second number field is empty")

# User input not empty
# Validation check i.e. make sure the user input contain only numeric values i.e. positive or negative
# Add two numbers -- Check whether the sum is odd or even number

if len(first_number) > 0 and len(second_number) > 0:
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
        sum = first_number + second_number

        if sum % 2 == 0:
            lines()
            print(f"First number: {first_number} plus Second number: {second_number} --> {sum}")
            print(f"{sum} is a even number")

        elif sum % 2 != 0:
            lines()
            print(f"First number: {first_number} plus Second number: {second_number} --> {sum}")
            print(f"{sum} is a odd number")
