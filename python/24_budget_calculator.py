#!/usr/bin/python
# Budget Calculator Script
# This script calculates total expenses and savings from user inputs.
# It also validates input for emptiness and numeric values.

def lines():
    print("*"*100)

# Get input from the user
total_income = input("Enter the total income:\n")
rent_cost = input("Enter the rent cost:\n")
groceries_cost = input("Enter the groceries cost:\n")
transport_cost = input("Enter the transport cost:\n")
utilities_cost = input("Enter the utilities cost:\n")
extra_cost = input("Enter the extra cost:\n")

# Check if any input is empty
if len(total_income) == 0 or len(rent_cost) == 0 or len(groceries_cost) == 0 or len(transport_cost) == 0 or len(utilities_cost) == 0 or len(extra_cost) == 0:
    lines()
    if len(total_income) == 0:
        print(f"User input --> Total income field is empty")
    if len(rent_cost) == 0:
        print(f"User input --> Rent cost field is empty")
    if len(groceries_cost) == 0:
        print(f"User input --> Groceries_cost field is empty")
    if len(transport_cost) == 0:
        print(f"User input --> Transport cost field is empty")
    if len(utilities_cost) == 0:
        print(f"User input --> Utilities cost field is empty")
    if len(extra_cost) == 0:
        print(f"User input --> Extra cost field is empty")

# user iput not empty
# Validate numeric input
# If any field is not numeric, show an error
# Convert all input strings to floats
# Calculate and display total cost and savings

elif len(total_income) >= 0 and len(rent_cost) >= 0 and len(groceries_cost) >= 0 and len(transport_cost) >= 0 and len(utilities_cost) >= 0 and len(extra_cost) >= 0:
    if not total_income.replace(".", "").isdigit() or not rent_cost.replace(".","").isdigit() or not groceries_cost.replace(".","").isdigit() or not transport_cost.replace(".", "").isdigit() or not utilities_cost.replace(".", "").isdigit() or not extra_cost.replace(".", "").isdigit():
        lines()
        if not total_income.replace(".", "").isdigit():
            print(f"Total income field must contain only numeric values")
        if not rent_cost.replace(".", "").isdigit():
            print(f"Rent cost field must contain only numeric values")
        if not groceries_cost.replace(".", "").isdigit():
            print(f"Groceries cost field must contain only numeric values")
        if not transport_cost.replace(".", "").isdigit():
            print(f"Transport cost field must contain only numeric values")
        if not utilities_cost.replace(".", "").isdigit():
            print(f"Utilities cost field must contain only numeric values")
        if not extra_cost.replace(".", "").isdigit():
            print(f"Extra cost field must contain only numeric values")

    elif total_income.replace(".", "").isdigit() and rent_cost.replace(".","").isdigit() and groceries_cost.replace(".","").isdigit() and transport_cost.replace(".", "").isdigit() and utilities_cost.replace(".", "").isdigit() and extra_cost.replace(".", "").isdigit():
        lines()
        total_income, rent_cost, transport_cost, groceries_cost, utilities_cost, extra_cost = float(total_income), float(rent_cost), float(transport_cost), float(groceries_cost), float(utilities_cost), float(extra_cost)

        total_cost = rent_cost + groceries_cost + transport_cost + utilities_cost + extra_cost
        savings = total_income - total_cost

        print(f"Total income --> {total_income}")
        print(f"Rent cost --> {rent_cost}")
        print(f"Groceries cost --> {groceries_cost}")
        print(f"Transport cost --> {transport_cost}")
        print(f"Utilities cost --> {utilities_cost}")
        print(f"Extra cost --> {extra_cost}")
        lines()
        print(f"Total cost --> {total_cost}")
        print(f"Savings --> {savings:.2f}")
