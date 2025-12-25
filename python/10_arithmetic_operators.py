#!/usr/bin/python

# Basic Arithmetic operators
# Function to print line i.e. separator line
def lines():
        print("*"*100)

# User input
first_number = input("Enter the first number:\n")
second_number = input("Enter the second number:\n")

# If user input missing 
if len(first_number) == 0 or len(second_number) == 0:
        lines()
        if len(first_number) == 0:
                print("User input --> First number field is empty")
        if len(second_number) == 0:
                print("User input --> Second number field is empty")

# User input 
# Validation check i.e. user input must contain only positive and negative numbers
# Validation pass -- Perofrm arithmetic operators 
elif len(first_number) > 0 and len(second_number) > 0:
        if not first_number.lstrip("-").isdigit() or not second_number.lstrip("-").isdigit():
                lines()
                if not first_number.lstrip("-").isdigit():
                        print("First number field must contain only numeric values")
                if not second_number.lstrip("-").isdigit():
                        print("Second number field must contain only numeric values")
        elif first_number.lstrip("-").isdigit() and second_number.lstrip("-").isdigit():
                lines()
                first_number = int(first_number)
                second_number = int(second_number)
                sum = first_number + second_number
                subtract = first_number - second_number
                multiply = first_number * second_number
                power = first_number ** second_number
                quotient = first_number / second_number
                quotient_rounding= first_number // second_number
                remainder = first_number % second_number


                print(f"First number: {first_number} plus Second number: {second_number} --> {sum}")
                print(f"First number: {first_number} minus Second number: {second_number} --> {subtract}")
                print(f"First number: {first_number} multiply Second number: {second_number} --> {multiply}")
                print(f"First number: {first_number} power Second number: {second_number} --> {power}")
                print(f"First number: {first_number} divide (Quotient) Second number: {second_number} --> {quotient}")
                print(f"First number: {first_number} divide (Quotient -- Rounding) Second number: {second_number} --> {quotient:.2f}")
                print(f"First number: {first_number} divide (Remainder) Second number: {second_number} --> {remainder}")
