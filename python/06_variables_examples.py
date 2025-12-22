# This script collects monthly income and different categories of expenses from the user, calculates the total expenses, and finally displays the savings.

# Input: Collecting monthly income
total_income = float(input("Enter the total income of the month: "))
# Input: Collecting expenses
rent = float(input("Enter the cost towards rent: "))
groceries = float(input("Enter the cost towards groceries: "))
transport = float(input("Enter the cost towards transport: "))
utilities = float(input("Enter the cost towards utilities such as internet, electricity and gas: "))
extra_cost = float(input("If any, enter extra cost: "))

# Calculations
total_expense = rent + groceries + transport + utilities + extra_cost
savings = total_income - total_expense

# Output: Display results
print(f"Total income -- {total_income}")
print(f"Total expense -- {total_expense:.2f}")
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

