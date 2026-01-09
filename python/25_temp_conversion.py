
def lines():
    print("*"*50)

# This Python script converts temperatures between Celsius and Fahrenheit.

# ---------------------- Celsius to Fahrenheit ----------------------
print("***************CELSIUS TO FAHRENHEIt***************")
celsius = input("Enter the temperature in celsius\n")

# Check for empty input
if len(celsius) == 0:
    lines()
    print(f"User input --> Celsius feild is empty")

# User input not empty
# User input validation 
# Validation pass -- do the calculation i.e. from celsius to fahrenheit 
else:
    if not celsius.replace(".","",1).lstrip("-").isdigit():
        lines()
        print("User input --> Celsius field must contain only numeric values")

    elif celsius.replace(".","",1).lstrip("-").isdigit():
        celsius = float(celsius)
        celsius_to_fahrenheit = (celsius * 9 / 5) + 32
        print(f"Temperature in Celsius --> {celsius}")
        print(f"Temperature in Fahrenheit --> {celsius_to_fahrenheit:.2f}")

print("***************FAHRENHEIT TO CELSIUS***************")
fahrenheit = input("Enter the temperature in fahrenheit\n")

if len(fahrenheit) == 0:
    lines()
    print(f"User input --> Fahrenheit feild is empty")

# User input not empty
# User input validation 
# Validation pass -- do the calculation i.e. from fahrenheit to celsius
else:
    if not fahrenheit.replace(".","",1).lstrip("-").isdigit():
        lines()
        print("User input --> Fahrenheit field must contain only numeric values")

    elif fahrenheit.replace(".","",1).lstrip("-").isdigit():
        fahrenheit = float(fahrenheit)
        fahrenheit_to_celsius = (fahrenheit - 32) * 5/9
        print(f"Temperature in Fahrenheit --> {fahrenheit}")
        print(f"Temperature in Celsius --> {fahrenheit_to_celsius:.2f}")
