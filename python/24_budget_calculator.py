#!/usr/bin/python

# Monthly Expense Calculator This script collects income and expense details from the user,
# validates the input, calculates total expenses, and shows savings.

def lines():
    print("*"*75)

# User input
total_income = input("Enter the total income\n")
rent_cost = input("Enter the rent cost\n")
groceries_cost = input("Enter the groceries cost\n")
transport_cost = input("Enter the transport cost\n")
utilities_cost = input("Enter the utilities cost such as electricity, phone, water, gas bill\n")
extra_cost = input("Enter the extra cost\n")

# User input empty
if len(total_income) == 0 or len(rent_cost) == 0 or len(groceries_cost) == 0 or len(transport_cost) == 0 or len(utilities_cost) == 0 or len(extra_cost) == 0:
    lines()
    if len(total_income) == 0:
        print("User input --> Total income field is empty")
    if len(rent_cost) == 0:
        print("User input --> Rent cost field is empty")
    if len(groceries_cost) == 0:
        print("User input --> Groceries cost field is empty")
    if len(transport_cost) == 0:
        print("User input --> Transport cost field is empty")
    if len(utilities_cost) == 0:
        print("User input --> Utilities cost field is empty")
    if len(extra_cost) == 0:
        print("User input --> Extra cost field is empty")
# user input not empty
# Validation check i.e. user input must be numeric value 
# validation passed --> convert the user ipnput from string to float data type
# Add all the expenses and subtract from total income 
# Display the results 
else:
    if not total_income.replace(".", "",1).isdigit() or not rent_cost.replace(".", "", 1).isdigit() or not groceries_cost.replace(".", "", 1).isdigit() or not transport_cost.replace(".", "", 1).isdigit() or not utilities_cost.replace(".", "", 1).isdigit() or not extra_cost.replace(".", "", 1).isdigit():
        lines()
        if not total_income.replace(".", "", 1).isdigit():
            print("Total income field must contain only numeric values")
        if not rent_cost.replace(".", "", 1).isdigit():
            print("Rent cost field must contain only numeric values")
        if not groceries_cost.replace(".", "", 1).isdigit():
            print("Groceries cost field must contain only numeric values")
        if not transport_cost.replace(".", "", 1).isdigit():
            print("Transport cost field must contain only numeric values")
        if not utilities_cost.replace(".", "", 1).isdigit():
            print("Utilities cost field must contain only numeric values")
        if not extra_cost.replace(".", "", 1).isdigit():
            print("Extra cost income field must contain only numeric values")
            
    else:
        lines()
        total_income, rent_cost, transport_cost = float(total_income), float(rent_cost), float(transport_cost)
        groceries_cost, utilities_cost, extra_cost = float(groceries_cost), float(utilities_cost), float(extra_cost)

        total_expenses = rent_cost + transport_cost + utilities_cost + groceries_cost + extra_cost
        savings = total_income - total_expenses


        print(f"Total income --> {total_income}")
        print(f"Rent cost --> {rent_cost}")
        print(f"Groceries cost --> {groceries_cost}")
        print(f"Transport cost --> {transport_cost}")
        print(f"Utilities cost --> {utilities_cost}")
        print(f"Extra cost --> {extra_cost}")

        print(f"Total expenses --> {total_expenses:.2f}")
        print(f"Savings --> {savings:.2f}")
