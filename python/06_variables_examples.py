#!/usr/bin/python

# basic program for variables 
# budget calculator 

# input from user 
savings = float(input("Enter the amount in savings: \n"))
rent_cost = float(input("Enter the rent cost: \n"))
groceries_cost = float(input("Enter the groceries cost: \n"))
transport_cost = float(input("Enter the transport cost: \n"))
utilities_cost = float(input("Enter the utilities cost: \n"))
extra_cost = float(input("Enter the extra cost, if any: \n"))

# calculate the total expenses 
total_cost = rent_cost + groceries_cost + transport_cost + utilities_cost + extra_cost
remaining_amount = savings - total_cost

# display output 
print("*"*75)
print(f"Savings --> {savings}")
print(f"Rent --> {rent_cost}")
print(f"Groceries --> {groceries_cost}")
print(f"Transport --> {transport_cost}")
print(f"Utilities --> {utilities_cost}")
print(f"Extra cost --> {extra_cost}")
print("*"*75)

print(f"Total expenses this month --> {total_cost}")
print(f"Remaining amount --> {remaining_amount:.2f}")

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

