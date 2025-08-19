#Python script for arithmetic operators

first_number=int(input("Enter the first number\n"))
second_number=int(input("Enter the first number\n"))

#Arithmetic operations such as addition, subtraction, multiplication, power, divide to find quotient and remainder
add=first_number+second_number
subtract=first_number-second_number
multiply=first_number*second_number
power=first_number**second_number
quotient_in_decimal=first_number/second_number
quotient_in_integer=first_number//second_number
remainder=first_number%second_number

print(f"Addition --> {first_number} plus {second_number} --> {add}")
print(f"Subtraction --> {first_number} subtract {second_number} --> {subtract}")
print(f"Multiply --> {first_number} multiply {second_number} --> {multiply}")
print(f"Power -->  {first_number} power {second_number} --> {power}")
print(f"Quotient in decimal --> {first_number} divide {second_number} --> {quotient_in_decimal}")
print(f"Quotient in integer --> {first_number} divide {second_number} --> {quotient_in_integer}")
print(f"Remainder {first_number} divide {second_number} --> {remainder}")



