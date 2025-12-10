# This Python script is a multiplication step generator designed to help beginners 
# understand how multiplication grows when the multiplier increases one step at a time
# Multiplicand → The base number that remains constant
# Multiplier → The starting number that will be incremented 
#Stop Number → A target value used to determine when to stop generating results

def lines():
    print("*"*100)

# User input
multiplicand = input("Enter the multiplicand number\n")
multiplier = input("Enter the multiplier number\n")
stop_number = input("Enter the stop number\n")

# If user input is empty
if len(multiplicand) == 0 or len(multiplier) == 0 or len(stop_number) == 0:
    if len(multiplicand) > 0 and len(multiplier) == 0 and len(stop_number) == 0:
        lines()
        print("User input -- Multiplier field is empty")
        print("User input -- Stop number field is empty")
    elif len(multiplicand) > 0 and len(multiplier) > 0 and len(stop_number) == 0:
        lines()
        print("User input -- Stop number field is empty")
    elif len(multiplicand) > 0 and len(multiplier) == 0 and len(stop_number) > 0:
        lines()
        print("User input -- Multiplier field is empty")
    elif len(multiplicand) == 0 and len(multiplier) > 0 and len(stop_number) > 0:
        lines()
        print("User input -- Multiplicand field is empty")

    elif len(multiplicand) == 0 and len(multiplier) == 0 and len(stop_number) > 0:
        lines()
        print("User input -- Multiplicand field is empty")
        print("User input -- Multiplier field is empty")

    elif len(multiplicand) == 0 and len(multiplier)> 0 and len(stop_number) == 0:
        lines()
        print("User input -- Multiplicand field is empty")
        print("User input -- Stop number field is empty")
    elif len(multiplicand) == 0 and len(multiplier) == 0 and len(stop_number) == 0:
        lines()
        print("User input -- Multiplicand field is empty")
        print("User input -- Multiplier field is empty")
        print("User input -- Stop number field is empty")

# User is not empty
# Validation -- Make sure the user input contain only postive numeric values
# Validation passes, multiplication using while loop 
# Multiplication stop when its greater than the stop number

elif len(multiplicand) > 0 and len(multiplier) > 0 and len(stop_number) > 0:
    if not multiplicand.isdigit() or not multiplier.isdigit() or not stop_number.isdigit():
        if multiplicand.isdigit() and not multiplier.isdigit() and not stop_number.isdigit():
            lines()
            print("Multiplier field must contain only positive numeric values")
            print("Stop number field must contain only positive numeric values")
        elif multiplicand.isdigit() and multiplier.isdigit() and not stop_number.isdigit():
            lines()
            print("Stop number field must contain only positive numeric values")
        elif multiplicand.isdigit() and not multiplier.isdigit() and stop_number.isdigit():
            lines()
            print("Multiplier field must contain only positive numeric values")
        elif not multiplicand.isdigit() and multiplier.isdigit()  and stop_number.isdigit():
            lines()
            print("Multiplicand field must contain only positive numeric values")
        elif not multiplicand.isdigit() and not multiplier.isdigit() and stop_number.isdigit():
            lines()
            print("Multiplicand field must contain only positive numeric values")
            print("Multiplier field must contain only positive numeric values")
        elif not multiplicand.isdigit() and multiplier.isdigit() and not stop_number.isdigit():
            lines()
            print("Multiplicand field must contain only positive numeric values")
            print("Stop field must contain only positive numeric values")
        elif not multiplicand.isdigit() and not multiplier.isdigit() and not stop_number.isdigit():
            lines()
            print("Multiplicand field must contain only positive numeric values")
            print("Multiplier field must contain only positive numeric values")
            print("Stop field must contain only positive numeric values")

    elif multiplicand.isdigit() and multiplier.isdigit() and stop_number.isdigit():
        multiplicand = int(multiplicand)
        multiplier = int(multiplier)
        stop_number = int(stop_number)

        multiply_result = multiplicand * multiplier

        if multiply_result == stop_number:
            lines()
            print(f"Multiplicand: {multiplicand} times Multiplier: {multiplier} --> {multiply_result}")
            print("Nothing to do")

        elif multiply_result > stop_number:
            lines()
            print(f"Multiplicand: {multiplicand} times Multiplier: {multiplier} --> {multiply_result}")
            print("Nothing to do")

        elif multiply_result < stop_number:
            lines()
            while multiply_result < stop_number:
                print(f"Multiplicand: {multiplicand} times Multiplier: {multiplier} --> {multiply_result}")
                multiplier+=1
                multiply_result = multiplicand * multiplier





