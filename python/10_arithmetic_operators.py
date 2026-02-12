#!/usr/bin/python
# basic arithmetic operators

# function to print lines
def lines():
    print("*"*100)

# user input
first_number = input("Enter the first number:\n")
second_number = input("Enter the second number:\n")

# user input empty
if len(first_number) == 0 or len(second_number) == 0:
    lines()
    if len(first_number) == 0:
        print("User input --> First number field is empty")
    if len(second_number) == 0:
        print("User input --> Second number field is empty")

# user input is not empty
# validate user input i.e. it must be an integer value other than 0
# validation pass, perform arithmetic operations
else:
    lines()
    if not first_number.lstrip("-").isdigit() or not second_number.lstrip("-").isdigit():
        if not first_number.lstrip("-").isdigit():
            print("First number field must contain integer values")
        if not second_number.lstrip("-").isdigit():
            print("Second number field must contain integer values")
    else:
        first_number, second_number = int(first_number), int(second_number)

        if first_number == 0 or second_number == 0:
            if first_number == 0:
                print("First number cannot be a zero integer number")
            if second_number == 0:
                print("Second number cannot be a zero integer number")

        else:
            sum = first_number + second_number
            subtract = first_number - second_number
            multiply = first_number * second_number
            power = first_number ** second_number
            quotient = first_number / second_number
            remainder = first_number % second_number

            print(f"{first_number} plus {second_number} --> {sum}")
            print(f"{first_number} subtract {second_number} --> {subtract}")
            print(f"{first_number} multiply {second_number} --> {multiply}")
            print(f"{first_number} power {second_number} --> {power}")
            print(f"{first_number} divide (quotient) {second_number} --> {quotient}")
            print(f"{first_number} divide (remainder) {second_number} --> {remainder:.2f}")
