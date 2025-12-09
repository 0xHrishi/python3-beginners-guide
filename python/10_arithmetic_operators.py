
# Function --> Print a separator line for cleaner output
def lines():
    print("*"*50)

# Take user input
first_number = input("Enter the first number:\n")
second_number = input("Enter the second number:\n")

# ----------------- CHECK FOR EMPTY INPUTS -----------------
if len(first_number) == 0 or len(second_number) == 0:
    if len(first_number) > 0 and len(second_number) ==0:
        lines()
        print("User input -- Second number field is empty")
    elif len(first_number) == 0 and len(second_number) > 0:
        lines()
        print("User input -- First number field is empty")
    if len(first_number) == 0 and len(second_number) == 0:
        lines()
        print("User input -- First number field is empty")
        print("User input -- Second number field is empty")

# ----------------- BOTH INPUTS PRESENT -----------------
# Check if inputs are numeric (allow negative values using strip)
# If both inputs are valid numbers
# Convert to integer
# Perform operations
# Print all results

elif len(first_number) > 0 and len(second_number) > 0:
    if not first_number.strip("-").isdigit() or not second_number.strip("-").isdigit():
        if first_number.strip("-").isdigit() and not second_number.strip("-").isdigit():
            lines()
            print("User input -- Second number field must contain only numeric values")
        elif not first_number.strip("-").isdigit() and second_number.strip("-").isdigit():
            lines()
            print("User input -- First number field must contain only numeric values")
        elif not first_number.strip("-").isdigit() and not second_number.strip("-").isdigit():
            lines()
            print("User input -- First number field must contain only numeric values")
            print("User input -- Second number field must contain only numeric values")

    elif first_number.strip("-").isdigit() and second_number.strip("-").isdigit():
        lines()
        first_number, second_number = int(first_number), int(second_number)
        sum = first_number + second_number
        subtract = first_number - second_number
        multiply = first_number * second_number
        power = first_number ** second_number
        quotient = first_number / second_number
        remainder = first_number % second_number
        print(f"First number: {first_number} plus Second number: {second_number} --> {sum}")
        print(f"First number: {first_number} subtract Second number: {second_number} --> {subtract}")
        print(f"First number: {first_number} multiply Second number: {second_number} --> {multiply}")
        print(f"First number: {first_number} power Second number: {second_number} --> {power}")
        print(f"First number: {first_number} divide (Quotient) Second number: {second_number} --> {quotient}")
        print(f"First number: {first_number} divide (Quotient) Second number: {second_number} --> {quotient:.2f}")
        print(f"First number: {first_number} divide (Remainder) Second number: {second_number} --> {remainder}")


