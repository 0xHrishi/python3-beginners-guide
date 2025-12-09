# Basic arithmetic operations
# Add, subtract, Multiplication, Division (Quotient and Remainder), power

def lines():
    print("*"*50)

# Prompt user for input
first_number = input("Enter the first number\n")
second_number = input("Enter the second number\n")

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

# User input is not empty
# with the help of .lstrip() and .isdigit() string method -- Make sure the user input must be only numeric value
# Special characters and alphabets not allowed
# If user input passes the validation -- Perform arithmetic operations 

elif len(first_number) > 0 and len(second_number)>0:
    if not first_number.lstrip("-").isdigit() or not second_number.lstrip("-").isdigit():
        if first_number.lstrip("-").isdigit() and not second_number.lstrip("-").isdigit():
            lines()
            print("Second number field must contain only numeric values(positive or negative)")
        elif not first_number.lstrip("-").isdigit() and second_number.lstrip("-").isdigit():
            lines()
            print("First number field must contain only numeric values(positive or negative)")
        elif first_number.lstrip("-").isdigit() and second_number.lstrip("-").isdigit():
            lines()
            print("First number field must contain only numeric values(positive or negative)")
            print("Second number field must contain only numeric values(positive or negative)")

    if first_number.lstrip("-").isdigit() and second_number.lstrip("-").isdigit():
        first_number = int(first_number)
        second_number = int(second_number)

        add = first_number + second_number
        sub = first_number - second_number
        multiply = first_number * second_number
        power = first_number ** second_number
        quotient = first_number / second_number
        remainder = first_number % second_number

        print(f"First number: {first_number} Addition Second number: {second_number} --> {add}")
        print(f"First number: {first_number} Subtract Second number: {second_number} --> {sub}")
        print(f"First number: {first_number} Multiply Second number: {second_number} --> {multiply}")
        print(f"First number: {first_number} Power Second number: {second_number} --> {power}")
        print(f"First number: {first_number} Divide (Quotient) Second number: {second_number} --> {quotient}")
        print(f"First number: {first_number} Divide (Quotient) Second number: {second_number} --> {quotient:.2f}")
        print(f"First number: {first_number} Divide (Remainder) Second number: {second_number} --> {remainder}")



