#!/usr/bin/python

def lines():
    print("*"*100)

# This script converts:
# 1) Celsius to Fahrenheit
# 2) Fahrenheit to Celsius

# user input
celsius = input("Enter the temperature in celsius\n")

lines()
# User input empty
if len(celsius) == 0:
    print("User input --> Temperature in celsius field is empty")

# User input not empty
# Validation check i.e. user input must contain only numeric values 
# validation passed -- convert the user input data type from string to float
# calculate and display 
else:
    if not celsius.replace(".", "", 1).isdigit():
        print("Temperature in celsius field must contain only numeric values")
    else:
        celsius = float(celsius)
        celsius_to_fahrenheit = (celsius * 9 / 5) + 32
        print(f"Temperature in celsius --> {celsius}")
        print(f"Temperature in fahrenheit --> {celsius_to_fahrenheit:.2f}")

lines()
# User input empty
fahrenheit = input("Enter the temperature in fahrenheit\n")

lines()
# user input empty
if len(fahrenheit) == 0:
    print("User input --> Temperature in fahrenheit field is empty")

# User input not empty
# Validation check i.e. user input must contain only numeric values 
# validation passed -- convert the user input data type from string to float
# calculate and display 
else:
    if not fahrenheit.replace(".", "", 1).isdigit():
        print("Temperature in fahrenheit field must contain only numeric values")
    else:
        fahrenheit = float(fahrenheit)
        fahrenheit_to_celsius =  (fahrenheit - 32) * 5 / 9
        print(f"Temperature in fahrenheit --> {fahrenheit}")
        print(f"Temperature in celsius --> {fahrenheit_to_celsius}")
