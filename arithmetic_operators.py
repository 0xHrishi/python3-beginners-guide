# Take input from the user for two numbers
first_number=input("Enter the first number\n")
second_number=input("Enter the second number\n")

# Function to print a line separator for readability
def lines():
    print("*"*50)

# Check if either or both inputs are empty
if len(first_number) == 0 or len(second_number) == 0:
    if len(first_number) > 0 and len(second_number) == 0:
        lines()
        print("User input -- Second number field is empty")
    elif len(first_number) == 0 and len(second_number) > 0:
        lines()
        print("User input -- First number field is empty")
    elif len(first_number) == 0 and len(second_number) == 0:
        lines()
        print("User input -- First number field is empty")
        print("User input -- Second number field is empty")

# When both inputs are provided
# Check if both inputs are valid integers (positive or negative)
# both inputs are valid numeric values (including negatives)
# Perform all arithmetic operations

elif len(first_number) > 0 and len(second_number) > 0:
    if not first_number.lstrip('-').isdigit() or not second_number.lstrip('-').isdigit():
        if first_number.lstrip('-').isdigit() and not second_number.lstrip('-').isdigit():
            lines()
            print("Second number field must contain only numeric values")
        elif not first_number.lstrip('-').isdigit() and second_number.lstrip('-').isdigit():
            lines()
            print("First number field must contain only numeric values")
        elif not first_number.lstrip('-').isdigit() and not second_number.lstrip('-').isdigit():
            lines()
            print("First number field must contain only numeric values")
            print("Second number field must contain only numeric values")
            
    elif first_number.lstrip('-').isdigit() and second_number.lstrip('-').isdigit():
        first_number=int(first_number)
        second_number=int(second_number)

        lines()
        add = first_number + second_number
        subtract = first_number - second_number
        multiply = first_number * second_number
        power = first_number ** second_number
        quotient = first_number / second_number
        remainder = first_number % second_number

        print(f"First number: {first_number} plus Second number: {second_number} --> {add}")
        print(f"First number: {first_number} minus Second number: {second_number} --> {subtract}")
        print(f"First number: {first_number} multiply Second number: {second_number} --> {multiply}")
        print(f"First number: {first_number} power Second number: {second_number} --> {power}")
        print(f"First number: {first_number} divide (quotient) Second number: {second_number} --> {quotient:.2f}")
        print(f"First number: {first_number} divide (remainder) Second number: {second_number} --> {remainder}")

