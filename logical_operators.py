#Python script to calculate the down payment for the house based upon the total cost and the credit score

total_cost=int(input("Enter the total cost of the house\n"))
credit_score=int(input("Enter the credit score\n"))

#Credit score greather than 750
if credit_score >= 750:
    print(f"Total cost of the house --> {total_cost}")
    print(f"Credit score --> {credit_score}")
    down_payment=total_cost*10/100
    print(f"Down payment --> {down_payment}")

#Credit score greather than eqaul to 650 and less than equal to 749
elif credit_score >=650 and credit_score<=749:
    print(f"Total cost of the house --> {total_cost}")
    print(f"Credit score --> {credit_score}")
    down_payment=total_cost*20/100
    print(f"Down payment --> {down_payment}")

#Credit score greather than eqaul to 600 and less than equal to 649

elif credit_score >= 600 and credit_score<=649:
    print(f"Total cost of the house --> {total_cost}")
    print(f"Credit score --> {credit_score}")
    down_payment=total_cost*30/100
    print(f"Down payment --> {down_payment}")

#Credit score less than 600
else:
    print("Cannot proceed with the application for now")
