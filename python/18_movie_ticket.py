# This script calculates the final ticket price after applying discounts based on the user's age and whether they have a loyalty card.
def lines():
    print("*"*100)

# Function -- final_cost
# Calculate the final cost based upon the ticket price, age and loyalty card
def final_cost():
    lines()
    print(f"Ticket cost -- {ticket_price}")
    print(f"Discount applied based upon age and loyalty card --> {discount}")
    final_price = ticket_price - discount
    print(f"Amount to be paid --> {final_price}")


# User prompt 
ticket_price = input("Enter the ticket price\n")
age = input("Enter the age\n")
loyalty_card = input("Do you have loyalty card y/n? \n")

# User input missing 
if len(ticket_price) == 0 or len(age) == 0 or len(loyalty_card) == 0:
    lines()
    print("User input -- One or more user input field is missing")

# User input == not empty
# Moves to validation i.e. to make sure the ticket price and the age contain only numeric value
# If both price and age are valid numeric values

elif len(ticket_price) > 0 and len(age) > 0 and len(loyalty_card) > 0:
    if not ticket_price.isdigit() or not age.isdigit():

        if not ticket_price.isdigit() and not age.isdigit():
            lines()
            print(f"Ticket price field must contain only numeric values")
            print(f"Age field must contain only numeric values")

        elif not ticket_price.isdigit() and age.isdigit():
            lines()
            print(f"Ticket price field must contain only numeric values")

        elif not age.isdigit() and ticket_price.isdigit():
            lines()
            print(f"Age field must contain only numeric values")



    elif ticket_price.isdigit() and age.isdigit():
        ticket_price = float(ticket_price)
        age = int(age)

        if age >= 60 and age <= 74:
            if loyalty_card.isalpha():
                if loyalty_card == "yes":
                    discount = float(ticket_price) * 15 / 100
                    final_cost()
                elif loyalty_card == "no":
                    discount = float(ticket_price) * 10 / 100
                    final_cost()
                else:
                    lines()
                    print("User Input -- Loyalty card must be yes or no")

        elif age >= 75:
            if loyalty_card.isalpha():
                if loyalty_card == "yes":
                    discount = float(ticket_price) * 20 / 100
                    final_cost()

                elif loyalty_card == "no":
                    discount = float(ticket_price) * 15 / 100
                    final_cost()

                else:
                    lines()
                    print("User Input -- Loyalty card must be yes or no")


        elif age >= 12 and age <= 59:
            if loyalty_card.isalpha():
                if loyalty_card == "yes":
                    discount = float(ticket_price) * 5 / 100
                    final_cost()
                elif loyalty_card == "no":
                    print(f"Ticket cost -- {ticket_price}")
                    print(f"Amount to be paid --> {ticket_price}")

                else:
                    lines()
                    print("User Input -- Loyalty card must be yes or no")


        elif age < 12:
            lines()
            print(f"Not eligible")










