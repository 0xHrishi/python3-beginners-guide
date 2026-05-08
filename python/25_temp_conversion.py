#!/usr/bin/python

# basic program for temp conversion
# user input
celsius = float(input("Enter the temperature in celsius:\n"))

# formuale to convert the temperature from celsius to fahrenheit
celsius_to_fahrenheit = (celsius * 9 / 5) + 32

print(f"Temperature in celsius --> {celsius}")
print(f"Temperature in fahrenheit --> {celsius_to_fahrenheit}")


print("*"*50)
print("*"*50)

# user input
fahrenheit = float(input("Enter the temperature in Fahrenheit:\n"))

# formuale to convert the temperature from fahrenheit to celsius
fahrenheit_to_celsius = (fahrenheit - 32) * 5 / 9
print(f"Temperatuure in fahrenheit --> {fahrenheit}")
print(f"Temperatuure in celsius --> {fahrenheit_to_celsius}")
