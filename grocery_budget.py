total_grocery_budget=100
#constant 
GROCERY_TAX=5

milk=5
print("Milk cost --> 5$")
bread=10
print("Bread cost --> 10$")
butter=20
print("Butter cost --> 20$")

#Totalcost will add all the 3 items 
total_cost=milk+bread+butter

#tax calculation 
tax_on_items=total_cost*GROCERY_TAX/100
#reaming budget
reamining_budget=total_grocery_budget-total_cost-tax_on_items

print(f"Grocery tax (5%) applied on total: ${tax_on_items}")
print(f"Reaming budget after purchase and tax: {reamining_budget}")
