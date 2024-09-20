#!/usr/bin/python3
#script ask user for the total house cost and based upon the credit score, calculates the down payment 


price=input("Enter the cost of the house:\n")
credit_score=input("Enter the credit score:\n")

if(len(price)<=0) or (len(credit_score)<=0):
    if(len(price)>0) and (len(credit_score)<=0):
        print("Credit score field is empty")
    elif(len(price)<=0) and (len(credit_score)>0):
        print("Price field is empty")
    else:
        print("Issues with the user input")

elif(len(price)>0) and (len(credit_score)>0):
    if (int(credit_score)>=750):
        print("*"*30)
        down_payment=int(price)*10/100
        print("Cost of House is --> " + str(price))
        print("CRedit score is --> " + str(credit_score))
        print("Down Payment -->" + str(down_payment))
        print("*"*30)
    elif (int(credit_score)<750) and (int(credit_score)>=650):
        print("*"*30)
        down_payment=int(price)*20/100
        print("Cost of House is --> " + str(price))
        print("CRedit score is --> " + str(credit_score))
        print("Down Payment -->" + str(down_payment))
        print("*"*30)
    else:
        print("*"*30)
        print("Bad credit score")                                                   
        print("Re-apply in next 6 months")                                          
        print("*"*30) 
--------------------------------------------------------------------------------------------------------------------------------------
#!/usr/bin/python3

total=input("Enter the total cost of the house\n")
credit=input("Enter the Credit score\n")

if (len(total)<=0) or (len(credit)<=0):
    if (len(total)>0) and (len(credit)<=0):
        print("*" *20)
        print("Credit score field is empty")
    elif (len(total)<=0) and (len(credit)>0):
        print("*" *20)
        print("Total cost of the house field is empty")
    elif (len(total)<=0) and (len(credit)<=0):
        print("*" *20)
        print("Total cost of the house field is empty")
        print("Credit score field is empty")
    else:
        print("*" *20)
        print("Issues with the user input")
elif (len(total)>0) and (len(credit)>0):
    if not total.isdigit() or not credit.isdigit():
        if total.isdigit() and not credit.isdigit():
            print("*" *20)
            print("Credit score must contain only numeric digits")
        elif not total.isdigit() and credit.isdigit():
            print("*" *20)
            print("Total cost of the house must contain only numeric digits")
        elif not total.isdigit() and not credit.isdigit():
            print("*" *20)
            print("Total cost of the house must contain only numeric digits")
            print("Credit score must contain only numeric digits")
        else:
            print("*" *20)
            print("Issues with user input validation")
    elif total.isdigit() and credit.isdigit():
        if (int(credit)>=750):
            ans=int(total)*10/100
            print("*" *20)
            print("Total cost of the house " + str(total))
            print("Credit score " + str(credit))
            print("Down payment require " + str(ans))
        elif (int(credit)>=650) and (int(credit)<=749):
            ans=int(total)*20/100
            print("*" *20)
            print("Total cost of the house " + str(total))
            print("Credit score " + str(credit))
            print("Down payment require " + str(ans))
        elif (int(credit)>=600) and (int(credit)<=649):
            ans=int(total)*30/100
            print("*" *20)
            print("Total cost of the house " + str(total))
            print("Credit score " + str(credit))
            print("Down payment require " + str(ans))
        else:
            print("Cannot process this application")
