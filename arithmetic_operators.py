#Script --> Basic calculator

#User input, data type as integer
first_number=int(input("Enter the first number\n"))
second_number=int(input("Enter the second number\n"))

#Arithmetic calculation such as add, subtract, multiply and power
add = first_number + second_number
subtract = first_number - second_number
multiply = first_number * second_number
power = first_number ** second_number

#Arithmetic calculation such as divide to get quotient in float and integer, remainder 
#If second number is equal to zero, the program will crash with ZeroDivision Error
if second_number != 0:
    divide_float = first_number / second_number
    divide_integer = first_number // second_number
    remainder = first_number % second_number

    print(f"First number:{first_number} plus Second number:{second_number} --> {add}")
    print(f"First number:{first_number} minus Second number:{second_number} --> {subtract}")
    print(f"First number:{first_number} multiply Second number:{second_number} --> {multiply}")
    print(f"First number:{first_number} power Second number:{second_number} --> {power}")
    print(f"First number:{first_number} divide (Quotient in float) Second number:{second_number} --> {divide_float}")
    print(f"First number:{first_number} divide (Quotient in integer) Second number:{second_number} --> {divide_integer}")
    print(f"First number:{first_number} divide (Remainder) Second number:{second_number} --> {remainder}")
else:
    print("Second number cannot be zero")




