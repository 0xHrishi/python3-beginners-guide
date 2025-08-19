#This script for the budget calculation

income=int(input("Enter the total income\n"))

rent_cost=int(input("Enter the rent\n"))
transport_cost=int(input("Enter the transport cost\n"))
groceries_cost=int(input("Enter the groceries cost\n"))
utilies_cost=int(input("Enter the utilies cost\n"))
extra_cost=int(input("Enter the extra cost\n"))

#Add all the cost
total_cost=rent_cost+transport_cost+groceries_cost+utilies_cost+extra_cost
#Display saving buy subtracting income - total cost
savings=income-total_cost

print(f"Rent cost --> {rent_cost}")
print(f"Transport cost --> {transport_cost}")
print(f"Groceries cost --> {groceries_cost}")
print(f"Utilies cost --> {utilies_cost}")
print(f"Extra cost --> {extra_cost}")

print("\n")
print(f"Total cost --> {total_cost}")
print(f"Saving --> {savings}")
