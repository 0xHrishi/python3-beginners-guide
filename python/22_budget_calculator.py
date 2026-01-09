#!/usr/bin/python
# This script collects monthly expense details from the user and calculates
# the total expenses and savings based on the provided total income.

def lines():
    print("*" * 50)

# User input
total_cost = input("Enter the total amount\n")
rent_cost = input("Enter the rent cost\n")
groceries_cost = input("Enter the groceries cost\n")
utilities_cost = input("Enter the utilities cost (Internet, Phone bill, Electricity)\n")
transport_cost = input("Enter the transport cost\n")
extra_cost = input("Enter the extra cost\n")

# ---------------------- Empty Input Validation ----------------------
if len(total_cost) == 0 or len(rent_cost) == 0 or len(groceries_cost) == 0 or len(utilities_cost) == 0 or len(transport_cost) == 0 or len(extra_cost) == 0:
    lines()
    if len(total_cost) == 0:
        print("User input --> Total cost field is empty")

    if len(rent_cost) == 0:
        print("User input --> Rent cost field is empty")

    if len(groceries_cost) == 0:
        print("User input --> Groceries cost field is empty")

    if len(utilities_cost) == 0:
        print("User input --> Utilities cost field is empty")

    if len(transport_cost) == 0:
        print("User input --> Transport cost field is empty")

    if len(extra_cost) == 0:
        print("User input --> Extra cost field is empty")

# User input not empty
# User input validation i.e. must contain only numeric values
# Convert the user input into float for calculation
# Calculate total expenses and savings
# Display the output

elif len(total_cost) > 0 and len(rent_cost) > 0 and len(groceries_cost) > 0 and len(utilities_cost) > 0 and len(transport_cost) > 0 and len(extra_cost) > 0:
    lines()
    if not total_cost.replace(".", "", 1).isdigit():
        print(f"Total cost field must contain numeric values only")

    if not rent_cost.replace(".", "",1).isdigit():
        print(f"Rent cost field must contain numeric values only")

    if not groceries_cost.replace(".", "",1).isdigit():
        print(f"Groceries cost field must contain numeric values only")

    if not utilities_cost.replace(".", "",1).isdigit():
        print(f"Utilies cost field must contain numeric values only")

    if not transport_cost.replace(".", "",1).isdigit():
        print(f"Transport cost field must contain numeric values only")

    if not extra_cost.replace(".", "",1).isdigit():
        print(f"Extra cost field must contain numeric values only")

    if total_cost.replace(".", "", 1).isdigit() and rent_cost.replace(".", "",1).isdigit() and groceries_cost.replace(".", "",1).isdigit() and utilities_cost.replace(".", "",1).isdigit() and transport_cost.replace(".","",1).isdigit() and extra_cost.replace(".", "",1).isdigit():
            total_cost = float(total_cost)
            rent_cost = float(rent_cost)
            groceries_cost = float(groceries_cost)
            transport_cost = float(transport_cost)
            utilities_cost = float(utilities_cost)
            extra_cost = float(extra_cost)

            total_amount =  rent_cost + groceries_cost + transport_cost + utilities_cost + extra_cost
            savings = total_cost - total_amount

            lines()
            print(f"Total cost --> {total_cost}")
            print(f"Rent cost --> {rent_cost}")
            print(f"Groceries cost --> {groceries_cost}")
            print(f"Utilities cost --> {utilities_cost}")
            print(f"Transport cost --> {transport_cost}")
            print(f"Extra cost --> {extra_cost}")
            lines()
            print(f"Total cost --> {total_amount}")
            print(f"Savings --> {savings:.2f}")
