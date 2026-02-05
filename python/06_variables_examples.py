#!/usr/bin/python
# Description -- Basic program for budget calculator 
# Add all the expenses and subtract from the total income and at the end display savings
def lines():
    print("*"*75)

# Prompt user input
total_income = float(input("Enter the total income\n"))
rent_cost = float(input("Enter the rent cost\n"))
groceries_cost = float(input("Enter the groceries cost\n"))
transport_cost = float(input("Enter the transport cost\n"))
utilities_cost = float(input("Enter the Utilities cost such as water, electrcicity and phone bill\n"))
extra_cost = float(input("Enter the extra cost\n"))

# Add all the expense
total_expenses = rent_cost + groceries_cost + transport_cost + utilities_cost + extra_cost
# Subtract total income - total expense
savings = total_income - total_expenses

# Display user input
lines()
print(f"Total income -- {total_income}")
print(f"Rent cost -- {rent_cost}")
print(f"Groceries cost -- {groceries_cost}")
print(f"Transport cost -- {transport_cost}")
print(f"Utilities cost -- {utilities_cost}")
print(f"Extra cost -- {extra_cost}")
# Display total expenses and savings
print(f"Total expenses -- {total_expenses:.2f}")
print(f"Savings -- {savings:.2f}")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This script converts: 1) Celsius to Fahrenheit 2) Fahrenheit to Celsius

# Prompt user to enter the temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))
# Celsius to Fahrenheit Conversion
celsius_to_fahrenheit = (celsius * 9 / 5) + 32

print(f"Temperature in Celsius -- {celsius}")
print(f"Temperature in Fahrenheit -- {celsius_to_fahrenheit:.2f}")


# Prompt user to enter the temperature in Fahrenheit
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
# Fahrenheit to Celsius Conversion
fahrenheit_to_celsius = (fahrenheit - 32) * 5 / 9

print(f"Temperature in Fahrenheit -- {fahrenheit}")
print(f"Temperature in Celsius -- {fahrenheit_to_celsius:.2f}")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

