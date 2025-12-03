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
