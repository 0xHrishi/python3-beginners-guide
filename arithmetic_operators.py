first_number=int(input("Enter the first number\n"))
second_number=int(input("Enter the second number\n"))

add=first_number+second_number
subtract=first_number-second_number
multiply=first_number*second_number
power=first_number**second_number
divide_float=first_number/second_number
divide_integer=first_number//second_number
remainder=first_number%second_number

print(f"First number:{first_number} plus Second number:{second_number} --> {add}")
print(f"First number:{first_number} subtract Second number:{second_number} --> {subtract}")
print(f"First number:{first_number} multiply Second number:{second_number} --> {multiply}")
print(f"First number:{first_number} power Second number:{second_number} --> {power}")
print(f"First number:{first_number} divide Second number:{second_number} --> Quotient in float value {divide_float}")
print(f"First number:{first_number} divide Second number:{second_number} --> Quotient in float value {divide_float:.2f}")
print(f"First number:{first_number} divide Second number:{second_number} --> Quotient in integer value {divide_integer}")
print(f"First number:{first_number} divide Second number:{second_number} --> Remainder {remainder}")
