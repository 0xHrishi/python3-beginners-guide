#!/usr/bin/python

# Basic budget calculator
# function to display lines
def lines():
        print("*"*75)

# user input
savings = input("Enter the total savings:\n")
rent_cost = input("Enter the rent cost:\n")
groceries_cost = input("Enter the groceries cost:\n")
transport_cost = input("Enter the transport cost:\n")
utilities_cost = input("Enter the utilities cost:\n")
extra_cost = input("Enter the extra cost:\n")

lines()
# user input empty
if len(savings) == 0 or len(rent_cost) == 0 or len(groceries_cost) == 0 or len(transport_cost) == 0 or len(utilities_cost) == 0 or len(extra_cost) == 0:
        if len(savings) == 0:
                print(f"User input --> Total savings field is empty")
        if len(rent_cost) == 0:
                print(f"User input --> Rent cost field is empty")
        if len(groceries_cost) == 0:
                print(f"User input --> Groceries cost field is empty")

        if len(transport_cost) == 0:
                print(f"User input --> Transport cost field is empty")
        if len(utilities_cost) == 0:
                print(f"User input --> Utilities cost field is empty")
        if len(extra_cost) == 0:
                print(f"User input --> Extra cost field is empty")

# user input not empty
# validation check i.e. user input must contain only numeric values
# validation pass -- calculate budget
else:
        if not savings.replace(".","").isdigit() or not rent_cost.replace(".","").isdigit() or not groceries_cost.replace(".","").isdigit() or not transport_cost.replace(".","").isdigit() or not utilities_cost.replace(".","").isdigit() or not extra_cost.replace(".","").isdigit():
                if not savings.replace(".","").isdigit():
                        print("Savings field must contain numeric values")
                if not rent_cost.replace(".","").isdigit():
                        print("Rent cost field must contain numeric values")
                if not groceries_cost.replace(".","").isdigit():
                        print("Groceries cost field must contain numeric values")
                if not transport_cost.replace(".","").isdigit():
                        print("Transport cost field must contain numeric values")
                if not utilities_cost.replace(".","").isdigit():
                        print("Utilities cost field must contain numeric values")
                if not extra_cost.replace(".","").isdigit():
                        print("Cost field field must contain numeric values")
        else:
                savings, rent_cost, groceries_cost, transport_cost, utilities_cost, extra_cost = float(savings), float(rent_cost), float(groceries_cost), float(transport_cost), float(utilities_cost), float(extra_cost)
                total_cost = rent_cost + groceries_cost + transport_cost + utilities_cost + extra_cost
                amount_reamining = savings - total_cost
                lines()

                print(f"Savings --> {savings}")
                print(f"Rent cost --> {rent_cost}")
                print(f"Groceries cost --> {groceries_cost}")
                print(f"Transport cost --> {transport_cost}")
                print(f"Utilities cost --> {utilities_cost}")
                print(f"Extra cost --> {extra_cost}")
                print(f"Total cost --> {total_cost}")
                print(f"Amount reamining --> {amount_reamining}")
