#Script for budget calculator
#Total income --> user input
total_income=float(input("Enter the total income\n"))

#Costs
rent_cost=float(input("Enter the rent cost\n"))
groceries_cost=float(input("Enter the groceries cost\n"))
transport_cost=float(input("Enter the transport cost\n"))
utilies_cost=float(input("Enter the utilies cost\n"))
extra_cost=float(input("Enter the extra cost\n"))

#total cost 
total_expenses=rent_cost+groceries_cost+transport_cost+utilies_cost+extra_cost
#remaining after income cost - total expenses
remaining_budget=total_income-total_expenses

print(f"Total income --> {total_income}")
print(f"Total expenses --> {total_expenses}")
print(f"Reamining --> {remaining_budget}")
