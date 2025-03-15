#!/usr/bin/python

#User input total cost of the house, credit score and basedupon the user input, display the down payment amount

#user input
total_cost=input("Enter the total cost of the house:\n")
credit_score=input("Enter the credit score:\n")

#function
def lines():
    print("*"*50)

#check user input empty
if (len(total_cost)==0) or (len(credit_score)==0):
    if (len(total_cost)>0) and (len(credit_score)==0):
        lines()
        print("Credit score field is empty")
    elif (len(total_cost)==0) and (len(credit_score)>0):
        lines()
        print("Total cost field is empty")
    elif (len(total_cost)==0) and (len(credit_score)==0):
        lines()
        print("Total cost field is empty")
        print("Credit score field is empty")
    else:
        lines()
        print("Issues with the user input")

#user input is not empty
elif (len(total_cost)>0) and (len(credit_score)>0):

    #use input mus contain only numeric values
    if not total_cost.isdigit() or not credit_score.isdigit():
        if total_cost.isdigit() and not credit_score.isdigit():
            lines()
            print("Credit score field must contain only numeric values")
        elif not total_cost.isdigit() and credit_score.isdigit():
            lines()
            print("Total cost field must contain only numeric values")
        elif not total_cost.isdigit() and not credit_score.isdigit():
            lines()
            print("Total cost field must contain only numeric values")
            print("Credit score field must contain only numeric values")
        else:
            lines()

    #user input contain only numeric values
    elif total_cost.isdigit() and credit_score.isdigit():

        #down payment calculation
        if (int(credit_score)>999):
            lines
            print("Credit score cannot be greather than 999")
        elif (int(credit_score)<999) or (int(credit_score)==999):
            if (int(credit_score)>750) or (int(credit_score)==750):
                down_payment=int(total_cost)*10/100
                lines()
                print(f"Total cost of the house --> {total_cost}")
                print(f"Credit scrore --> {credit_score}")
                print(f"Down payment --> {down_payment}")
            elif (int(credit_score)>650) or (int(credit_score)==650):
                down_payment=int(total_cost)*20/100
                lines()
                print(f"Total cost of the house --> {total_cost}")
                print(f"Credit scrore --> {credit_score}")
                print(f"Down payment --> {down_payment}")
            elif (int(credit_score)>600) or (int(credit_score)==600):
                down_payment=int(total_cost)*30/100
                lines()
                print(f"Total cost of the house --> {total_cost}")
                print(f"Credit scrore --> {credit_score}")
                print(f"Down payment --> {down_payment}")
            else:
                lines()
                print("Cannot proceed the application")
