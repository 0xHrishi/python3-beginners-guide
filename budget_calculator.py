# ------------------------------------------------------------
# Program: Monthly Expense and Savings Calculator
# Description:
#     This program takes the user's total income and expenses 
#     (rent, groceries, transport, utilities, and extras)
#     then calculates total expenses and monthly savings.
# ------------------------------------------------------------

#Take user inputs
total_income = float(input("Enter the total income: "))

rent_cost = float(input("Enter the rent cost: "))
groceries_cost = float(input("Enter the groceries cost: "))
transport_cost = float(input("Enter the transport cost: "))
utilities_cost = float(input("Enter the utilities cost: "))
extra_cost = float(input("Enter the extra costs: "))

# Calculate total expenses
total_expenses = rent_cost + groceries_cost + transport_cost + utilities_cost + extra_cost

# Calculate savings
savings = total_income - total_expenses

# 🔹 Display results with proper formatting
print(f"\nTotal Income --> {total_income:.2f}")
print(f"Total Expenses --> {total_expenses:.2f}")
print(f"Savings --> {savings:.2f}")

